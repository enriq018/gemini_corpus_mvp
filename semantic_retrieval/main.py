import json
import os
import sys

# Manually adjust the sys.path at the top of the script to include the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Now import the necessary functions
from semantic_retrieval.utils.create_prompt import create_prompt
from semantic_retrieval.utils.gemini_api import gemini_api
from semantic_retrieval.dynamic_filter import query_with_dynamic_filters

json_object = {
  "relevent_lore": {
    "Characters": {
      "Caesar": ["Background", "Appearances"]
    }
  },
  "npc_modifiers": {
    "npc_role": "legion guard",
    "npc_personality": "happy",
    "conversation_context": "discussing how they support Ceasar",
    "conversation_tone": "Confident",
    "main_dialog_purpose": "Talking about their admiration for Ceasar"
  },
  "dialog_type": "single"
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

def generate_complete_response(json_object):
    npc_lore = json_object["relevent_lore"]
    npc_modifiers = json_object["npc_modifiers"]
    model = gemini_api()
    sematic_search_results = query_with_dynamic_filters(npc_lore)
    complete_prompt = create_prompt(sematic_search_results, npc_modifiers)
    response = model.generate_content(complete_prompt, safety_settings=safety_settings)
    print(response.text)
    return response.text


# generate_complete_response(json_object)