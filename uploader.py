import requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CLIENT_ID = os.getenv("YT_CLIENT_ID")
CLIENT_SECRET = os.getenv("YT_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("YT_REFRESH_TOKEN")

def get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    res = requests.post(url, data=data).json()
    return res["access_token"]

def upload(video_path, title, desc, schedule_time):
    access = get_access_token()

    youtube = build(
        "youtube", "v3",
        developerKey=None,
        credentials=None,
        requestBuilder=lambda *args, **kwargs: None
    )

    youtube._http.headers.update({
        "Authorization": f"Bearer {access}",
        "Accept": "application/json"
    })

    request = youtube.videos().insert(
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
        media_body=MediaFileUpload(video_path)
    )

    return request.execute()
