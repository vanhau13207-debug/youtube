from fb_scraper import get_reels_from_page
from video_editor import process_video
from concat_builder import build_30m
from uploader import upload
from title_desc import gen_title_desc
from utils import load_db, save_db, filter_new_videos, download

import datetime
import os

PAGE = "https://www.facebook.com/yourpage/videos"  # đổi link page của bạn vào

def run():
    urls = get_reels_from_page(PAGE, 50)
    new = filter_new_videos(urls)

    if not new:
        print("Không có video mới.")
        return

    processed = []

    for idx, url in enumerate(new[:20]):
        raw = f"raw_{idx}.mp4"
        out = f"edit_{idx}.mp4"

        download(url, raw)
        process_video(raw, out)

        processed.append(out)

    build_30m(processed, "final.mp4")

    title, desc = gen_title_desc()

    schedule = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).isoformat("T") + "Z"

    upload("final.mp4", title, desc, schedule)

    db = load_db()
    db["used"] += new[:20]
    save_db(db)

if __name__ == "__main__":
    run()
