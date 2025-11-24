import json, os
import yt_dlp

def load_db():
    if not os.path.exists("db.json"):
        return {"used": []}
    return json.load(open("db.json"))

def save_db(db):
    json.dump(db, open("db.json", "w"), indent=2)

def filter_new_videos(urls):
    db = load_db()
    return [u for u in urls if u not in db["used"]]

def download(url, output):
    ydl_opts = {"outtmpl": output, "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
