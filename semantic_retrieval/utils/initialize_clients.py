import json
import os
import sys

# Manually adjust the sys.path at the top of the script to include the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

import google.ai.generativelanguage as glm
from google.oauth2 import service_account

# Initialize credentials and client libraries
def initialize_clients():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to your service account key file
    service_account_file_name = os.path.join(current_dir, '..', 'credentials', 'geminiapideveloper-1623bba633a0.json')
    
    credentials = service_account.Credentials.from_service_account_file(service_account_file_name)
    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/generative-language.retriever']
    )
    generative_service_client = glm.GenerativeServiceClient(credentials=scoped_credentials)
    retriever_service_client = glm.RetrieverServiceClient(credentials=scoped_credentials)
    permission_service_client = glm.PermissionServiceClient(credentials=scoped_credentials)
    print("Client libraries initialized successfully.")
    return generative_service_client, retriever_service_client, permission_service_client
