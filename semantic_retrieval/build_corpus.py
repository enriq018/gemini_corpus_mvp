import os
import json
from transformers import GPT2Tokenizer
import google.ai.generativelanguage as glm
from google.oauth2 import service_account
import time

# Path to your service account key file
service_account_file_name = 'geminiapideveloper-1623bba633a0.json'

# Path to your directory containing JSON files
json_dir = 'scraped_data'

# Initialize credentials and client libraries
def initialize_clients(service_account_file_name):
    credentials = service_account.Credentials.from_service_account_file(service_account_file_name)
    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/generative-language.retriever']
    )
    generative_service_client = glm.GenerativeServiceClient(credentials=scoped_credentials)
    retriever_service_client = glm.RetrieverServiceClient(credentials=scoped_credentials)
    permission_service_client = glm.PermissionServiceClient(credentials=scoped_credentials)
    print("Client libraries initialized successfully.")
    return generative_service_client, retriever_service_client, permission_service_client

# Function to list all corpora
def list_corpora(retriever_service_client):
    request = glm.ListCorporaRequest()
    response = retriever_service_client.list_corpora(request)
    return response.corpora

# Function to check and create corpus
def check_and_create_corpus(retriever_service_client, corpus_name="Fallout New Vegas"):
    corpus_exists = False
    corpus_resource_name = None
    for corpus in list_corpora(retriever_service_client):
        if corpus.display_name == corpus_name:
            corpus_exists = True
            corpus_resource_name = corpus.name
            break
    if not corpus_exists:
        example_corpus = glm.Corpus(display_name=corpus_name)
        create_corpus_request = glm.CreateCorpusRequest(corpus=example_corpus)
        create_corpus_response = retriever_service_client.create_corpus(create_corpus_request)
        corpus_resource_name = create_corpus_response.name
        print("Corpus created successfully.")
    else:
        print("Corpus already exists.")
    print(f"Corpus Resource Name: {corpus_resource_name}")
    return corpus_resource_name

# Function to list documents in the corpus
def list_documents(retriever_service_client, corpus_resource_name):
    request = glm.ListDocumentsRequest(parent=corpus_resource_name)
    response = retriever_service_client.list_documents(request)
    return response.documents

# Function to list chunks in a document
def list_chunks(retriever_service_client, document_id):
    request = glm.ListChunksRequest(parent=document_id)
    response = retriever_service_client.list_chunks(request)
    return response.chunks

# Function to delete a chunk by its ID
def delete_chunk(retriever_service_client, chunk_id):
    try:
        request = glm.DeleteChunkRequest(name=chunk_id)
        retriever_service_client.delete_chunk(request)
        print(f"Chunk {chunk_id} deleted successfully.")
    except Exception as e:
        print(f"Failed to delete chunk {chunk_id}: {e}")

# Function to delete all chunks in a document
def delete_all_chunks(retriever_service_client, document_id):
    retries = 3
    while retries > 0:
        chunks = list_chunks(retriever_service_client, document_id)
        if not chunks:
            break
        for chunk in chunks:
            delete_chunk(retriever_service_client, chunk.name)
        time.sleep(2)  # Wait for a short time before checking again
        retries -= 1
    if retries == 0 and list_chunks(retriever_service_client, document_id):
        print(f"Failed to delete all chunks in document {document_id} after multiple attempts.")

# Function to delete a document by its ID
def delete_document(retriever_service_client, document_id):
    delete_all_chunks(retriever_service_client, document_id)
    try:
        request = glm.DeleteDocumentRequest(name=document_id)
        retriever_service_client.delete_document(request)
        print(f"Document {document_id} deleted successfully.")
    except Exception as e:
        print(f"Failed to delete document {document_id}: {e}")

# Function to create a document from a single JSON file
def create_document_from_json(retriever_service_client, corpus_resource_name, json_file):
    documents = list_documents(retriever_service_client, corpus_resource_name)
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        title = data.get('title')
        category = data.get('category')
        existing_doc = None
        for doc in documents:
            if doc.display_name == title and any(meta.string_value == category for meta in doc.custom_metadata):
                existing_doc = doc.name
                break
        if existing_doc:
            delete_document(retriever_service_client, existing_doc)
        if title and category:
            display_name = title
            document_metadata = [
                glm.CustomMetadata(key="category", string_value=category),
                glm.CustomMetadata(key="title", string_value=title)
            ]
            example_document = glm.Document(display_name=display_name)
            example_document.custom_metadata.extend(document_metadata)
            create_document_request = glm.CreateDocumentRequest(
                parent=corpus_resource_name, document=example_document)
            create_document_response = retriever_service_client.create_document(create_document_request)
            document_id = create_document_response.name
            print(f"Document created successfully: {document_id}")
            content_data = data['content']
            chunks = []
            for section, content in content_data.items():
                for part in split_into_chunks(content):
                    chunk = glm.Chunk(data={'string_value': part})
                    chunk.custom_metadata.append(glm.CustomMetadata(key="section_name", string_value=section))
                    chunks.append(chunk)
            create_chunk_requests = [glm.CreateChunkRequest(parent=document_id, chunk=chunk) for chunk in chunks]
            request = glm.BatchCreateChunksRequest(parent=document_id, requests=create_chunk_requests)
            response = retriever_service_client.batch_create_chunks(request)
            print(f"Chunks created successfully for document: {document_id}")

# Function to split text into chunks based on tokens
def split_into_chunks(text, max_tokens=300):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.tokenize(text)
    token_chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    for token_chunk in token_chunks:
        yield tokenizer.convert_tokens_to_string(token_chunk)

# Function to process all JSON files in the directory
def process_all_files(retriever_service_client, corpus_resource_name, json_dir):
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_dir, filename)
            print(f"Processing file: {json_file_path}")
            create_document_from_json(retriever_service_client, corpus_resource_name, json_file_path)

# Main execution
generative_service_client, retriever_service_client, permission_service_client = initialize_clients(service_account_file_name)
corpus_resource_name = check_and_create_corpus(retriever_service_client)
process_all_files(retriever_service_client, corpus_resource_name, json_dir)
