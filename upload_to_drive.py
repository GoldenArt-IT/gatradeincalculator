from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io
import streamlit as st

# Load credentials
SERVICE_ACCOUNT_FILE = st.secrets["gdrive"]
SCOPES = ["https://www.googleapis.com/auth/drive"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build("drive", "v3", credentials=credentials)

# Upload function
def upload_file_to_drive(file, filename, folder_id):
    file_metadata = {
        "name": filename,
        "parents": [folder_id]
    }
    media = MediaIoBaseUpload(io.BytesIO(file.read()), mimetype=file.type)

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded_file.get("id")

    # Make it public
    drive_service.permissions().create(
        fileId=file_id,
        body={"role": "reader", "type": "anyone"},
    ).execute()

    # Return shareable link
    return f"https://drive.google.com/uc?id={file_id}"
