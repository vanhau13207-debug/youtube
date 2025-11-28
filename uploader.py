from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import datetime, os

def upload(video_path, title, description, schedule_time):
    creds = Credentials(
        None,
        refresh_token=os.getenv("YT_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("YT_CLIENT_ID"),
        client_secret=os.getenv("YT_CLIENT_SECRET"),
        scopes=["https://www.googleapis.com/auth/youtube.upload"],
    )

    yt = build("youtube", "v3", credentials=creds)

    request = yt.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "24",
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": schedule_time
            }
        },
        media_body=MediaFileUpload(video_path)
    )

    response = request.execute()
    print("Uploaded:", response)
