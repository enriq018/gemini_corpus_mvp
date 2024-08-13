import os
import sys

# Add the root directory to sys.path to resolve module paths correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS
from server.routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Register the blueprint
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=port, debug=True)
