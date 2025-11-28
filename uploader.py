import os
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials


CLIENT_ID = os.getenv("YT_CLIENT_ID")
CLIENT_SECRET = os.getenv("YT_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("YT_REFRESH_TOKEN")

def get_youtube_client():
    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri="https://oauth2.googleapis.com/token"
    )
    return build("youtube", "v3", credentials=creds)

def upload(video_file, title, description, schedule_time):
    youtube = get_youtube_client()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "24"
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": schedule_time
            }
        },
        media_body=MediaFileUpload(video_file)
    )

    response = request.execute()
    print("UPLOAD DONE → VIDEO ID:", response["id"])
