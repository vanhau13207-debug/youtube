from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload(video, title, desc, schedule_time):
    yt = build("youtube", "v3", developerKey=os.getenv("YT_API"))

    request = yt.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": desc,
                "categoryId": "24"
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": schedule_time
            }
        },
        media_body=MediaFileUpload(video)
    )
    request.execute()
