import os
import sys

# Manually adjust the sys.path at the top of the script
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.append(project_root)

# Now import the helper function
from semantic_retrieval.utils.path_helpers import add_project_root_to_sys_path

# Use the helper function to ensure the project root is in sys.path
add_project_root_to_sys_path()


from google.ai.generativelanguage import GenerativeServiceClient, RetrieverServiceClient, ListDocumentsRequest, ListChunksRequest
from google.oauth2 import service_account
from semantic_retrieval.utils.initialize_clients import initialize_clients

generative_service_client, retriever_service_client, permission_service_client = initialize_clients()


# Corpus resource name (use the one you created earlier)
corpus_resource_name = 'corpora/fallout-new-vegas-4m240m01dlns'

# Function to list all documents and their metadata, handling pagination
def list_all_documents(corpus_resource_name):
    all_documents = []
    next_page_token = None
    
    while True:
        list_documents_request = ListDocumentsRequest(parent=corpus_resource_name, page_token=next_page_token)
        documents_response = retriever_service_client.list_documents(list_documents_request)
        
        for document in documents_response.documents:
            doc_metadata = {metadata.key: metadata.string_value for metadata in document.custom_metadata}
            all_documents.append({
                'name': document.name,
                'metadata': doc_metadata
            })
        
        next_page_token = documents_response.next_page_token
        if not next_page_token:
            break
    
    return all_documents

# Function to list all chunks and their metadata for a given document
def list_all_chunks(document_name):
    all_chunks = []
    next_page_token = None
    
    while True:
        list_chunks_request = ListChunksRequest(parent=document_name, page_token=next_page_token)
        chunks_response = retriever_service_client.list_chunks(list_chunks_request)
        
        for chunk in chunks_response.chunks:
            chunk_metadata = {metadata.key: metadata.string_value for metadata in chunk.custom_metadata}
            all_chunks.append({
                'metadata': chunk_metadata
            })
        
        next_page_token = chunks_response.next_page_token
        if not next_page_token:
            break
    
    return all_chunks

# Function to print all documents and their chunks' metadata
def print_all_documents_and_chunks_metadata():
    all_documents = list_all_documents(corpus_resource_name)
    
    print("All Documents and Their Metadata:")
    for document in all_documents:
        print(f"Document: {document['name']}")
        for key, value in document['metadata'].items():
            print(f"  Metadata - {key}: {value}")
        
        all_chunks = list_all_chunks(document['name'])
        print(f"Chunks for Document {document['name']}:")
        for chunk in all_chunks:
            for key, value in chunk['metadata'].items():
                print(f"    Metadata - {key}: {value}")

# Run the function to print all documents and chunks' metadata
print_all_documents_and_chunks_metadata()
