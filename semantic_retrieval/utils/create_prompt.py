import json

def create_prompt(context_data, npc_modifiers):
    # Extract main_dialog_purpose separately
    main_dialog_purpose = npc_modifiers.pop("main_dialog_purpose", "Slice of life")
    
    prompt_template = """
    Use the following as context:

    {context}

    Provide me with 3-4 sentences of NPC dialog.
    {main_dialog_purpose}
    Here is some helpful information:
    {modifiers_list}

    OUTPUT: Return only dialog as a string
    """

    # Dynamically create the list of modifiers
    modifiers_list = ""
    for key, value in npc_modifiers.items():
        if key != "conversation_focus":
            modifiers_list += f"- {key.replace('_', ' ').capitalize()}: {value}\n"

    # Create the prompt
    prompt = prompt_template.format(
        context=json.dumps(context_data, indent=2),
        main_dialog_purpose=main_dialog_purpose,
        conversation_focus=npc_modifiers.get("conversation_focus", ""),
        modifiers_list=modifiers_list
    )

    return prompt

# Example usage
context_data = {
    "Characters": {
        "Benny": {
            "Background": ["Background text here..."],
            "Notes": ["Notes text here..."]
        }
    },
    "Locations": {
        "Camp McCarran": {
            "Background": ["Background text here..."],
            "Notes": ["Notes text here..."]
        }
    }
}

npc_modifiers = {
  "npc_role": "guard",
  "npc_personality": "stern",
  "conversation_context": "player asking for directions",
  "main_dialog_purpose": "The player needs guidance to find a hidden location.",
  "player_reputation": "neutral",
  "player_history": "first interaction",
  "location": "town square",
  "location_significance": "central hub",
  "conversation_tone": "informative",
  "npc_name": "Sergeant Knox",
  "player_objective": "find the hidden treasure",
  "conversation_focus": "The player is looking for directions to a hidden location."
}

# prompt = create_prompt(context_data, npc_modifiers)
# print(prompt)
