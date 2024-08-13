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

import google.ai.generativelanguage as glm
from semantic_retrieval.utils.initialize_clients import initialize_clients

generative_service_client, retriever_service_client, permission_service_client = initialize_clients()


# Function to list all corpora
def list_corpora():
    request = glm.ListCorporaRequest()
    response = retriever_service_client.list_corpora(request)
    return response.corpora

# List and print all corpora
corpora = list_corpora()
for corpus in corpora:
    print(f"Corpus ID: {corpus.name}, Display Name: {corpus.display_name}")

