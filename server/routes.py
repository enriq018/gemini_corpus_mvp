from flask import Blueprint, request, jsonify
from semantic_retrieval.main import generate_complete_response
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/npc', methods=['POST'])
def npc_dialog_handler():
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")

        # Validate input data
        if not data:
            logging.error("No data received")
            return jsonify({"error": "Invalid input: No data received"}), 400

        relevent_lore = data.get('relevent_lore')
        npc_modifiers = data.get('npc_modifiers')

        if not relevent_lore:
            logging.error("relevent_lore not found in data")
            return jsonify({"error": "Invalid input: 'relevent_lore' is required"}), 400
        if not npc_modifiers:
            logging.error("npc_modifiers not found in data")
            return jsonify({"error": "Invalid input: 'npc_modifiers' is required"}), 400

        # Generate response
        response_text = generate_complete_response(data)
        logging.debug(f"Response data: {response_text}")

        return jsonify({"response": response_text})

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500
