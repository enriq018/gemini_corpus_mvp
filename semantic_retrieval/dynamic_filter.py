import json
import os
import sys

# Manually adjust the sys.path at the top of the script to include the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)


from google.ai.generativelanguage import GenerativeServiceClient, RetrieverServiceClient, QueryCorpusRequest, MetadataFilter, Condition
from semantic_retrieval.utils.initialize_clients import initialize_clients

generative_service_client, retriever_service_client, permission_service_client = initialize_clients()


# Corpus resource name (use the one you created earlier)
corpus_resource_name = 'corpora/fallout-new-vegas-4m240m01dlns'

def create_metadata_filters(category, titles):
    metadata_filters = []

    # Category filter
    metadata_filters.append(
        MetadataFilter(
            key="document.custom_metadata.category",
            conditions=[Condition(string_value=category, operation=Condition.Operator.EQUAL)]
        )
    )
    for title, sections in titles.items():
        # Title filter
        metadata_filters.append(
            MetadataFilter(
                key="document.custom_metadata.title",
                conditions=[Condition(string_value=title, operation=Condition.Operator.EQUAL)]
            )
        )
        # Group all section conditions under a single filter
        section_conditions = [
            Condition(string_value=section, operation=Condition.Operator.EQUAL) for section in sections
        ]
        metadata_filters.append(
            MetadataFilter(
                key="chunk.custom_metadata.section_name",
                conditions=section_conditions
            )
        )

    return metadata_filters

def query_with_dynamic_filters(npc_json):
    organized_data = {}

    for category, titles in npc_json.items():
        for title, sections in titles.items():
            organized_data.setdefault(category, {}).setdefault(title, {})

            metadata_filters = create_metadata_filters(category, {title: sections})

            request = QueryCorpusRequest(
                name=corpus_resource_name,
                query="Tell me about these topics",
                results_count=5,
                metadata_filters=metadata_filters
            )

            query_corpus_response = retriever_service_client.query_corpus(request)

            # Organize relevant chunks
            for result in query_corpus_response.relevant_chunks:
                # Print metadata for debugging
                # print("Chunk metadata:")
                # for metadata in result.chunk.custom_metadata:
                #     print(f"{metadata.key}: {metadata.string_value}")

                # Extract section_name from metadata
                section_name = "Unknown"
                for metadata in result.chunk.custom_metadata:
                    if metadata.key == "section_name":
                        section_name = metadata.string_value
                        break

                if section_name not in organized_data[category][title]:
                    organized_data[category][title][section_name] = []
                # Add only the first 5 characters of the chunk value
                organized_data[category][title][section_name].append(result.chunk.data.string_value)

    return json.dumps(organized_data, indent=4)