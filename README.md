# README
### Demo:
https://www.youtube.com/watch?v=KFucmF2YWrU

## Content Market Scripts

This README provides instructions on how to set up and run the `gemCorp` environment and main script.

### Prerequisites

- Conda installed on your machine.

### Setup Instructions

1. **Open Conda Terminal** - Launch the Conda terminal on your computer.

2. **Navigate to the Project Directory** - Change your directory to the project location by running the following command:

   ```bash
   cd D_Desk\ai_projects\gemComp\mvpCorp
   ```

3. **Activate the Conda Environment** - Activate the `gemCorp` environment by running:
   ```bash
   conda activate gemCorp
   ```

### Running the Main Script

To execute the main script, run the following command in the terminal:

```bash
python main.py
```

---

To run server:

```bash
python server/app.py
```

Make a POST to http://localhost:8080/npc

### To Dos

filtering doesnt have any checking. we are assuming that tags will be fully completed when sent.

Ex: For location, must be title and a section_name
Location -> Cantina Madrid -> Layout

1. **Google create documents and chunks** - Create a `.env` file in the project root to store environment-specific variables.

---

Semantic search guide: https://ai.google.dev/gemini-api/docs/semantic_retrieval
Service key instructions: https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount

^ i think that makes the file we place in credentials ie: geminiapideveloper-1623bba633a0.json

Sure! Here are the steps we took from building the Docker image to deploying it on Google Cloud Run, followed by uploading the `ui` folder to Google Cloud Storage:

### Docker Deployment and UI Hosting Steps

#### Building and Deploying the Docker Image to Google Cloud Run

1. **Build the Docker Image**:

   Navigate to the root directory of your new app project and build the Docker image:

   ```bash
   docker build -t gcr.io/onet-rag/npc_rag_server:latest .
   ```

2. **Push the Docker Image to Google Container Registry**:

   Push the Docker image to your Google Container Registry:

   ```bash
   docker push gcr.io/onet-rag/npc_rag_server:latest
   ```

3. **Deploy to Google Cloud Run**:

   Deploy the server to Google Cloud Run using the following command:

   ```bash
   gcloud run deploy npc-rag-server --image gcr.io/onet-rag/npc_rag_server:latest --platform managed --region us-west1 --allow-unauthenticated
   ```

   This command deploys the Docker image to Google Cloud Run, allowing the service to be accessed publicly.

#### Setting Up and Serving the UI from Google Cloud Storage

4. **Upload the `ui` Folder to Google Cloud Storage**:

   Upload the contents of the `ui` folder to your existing Google Cloud Storage bucket using the Google Cloud Console:

   - Navigate to your bucket in the Google Cloud Console.
   - Upload all files (`index.html`, `api.js`, `master_tags.js`, `scripts.js`, `styles.css`) from the `ui` folder.

5. **Make the Files Public**:

   - Select all the uploaded files.
   - Click on the "Permissions" tab.
   - Add a new permission for `allUsers` with the role `Storage Object Viewer`.

6. **Set the Bucket as a Public Website**:

   - In the Google Cloud Console, go to the bucket settings.
   - Under the "Website configuration" section, set the "Main page suffix" to `index.html`.

7. **Access Your HTML File**:

   Access the `index.html` file using the URL format:

   ```
   https://storage.googleapis.com/your-bucket-name/index.html
   ```

### Summary

These steps guide you through building, pushing, and deploying a Docker image for your new app to Google Cloud Run, and then uploading and serving your UI files from Google Cloud Storage. By following these steps, you can ensure a smooth deployment and access to your application's frontend.

Feel free to copy and paste this into your README file. If you need further assistance or modifications, let me know!
