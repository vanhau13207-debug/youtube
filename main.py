from fb_scraper import get_from_multiple_pages
from util_db import load_db, save_db, filter_new_videos
from downloader import download
from video_editor import process_video
from concat_builder import build_30m
from title_desc import gen_title_desc
from uploader import upload
import datetime, os

PAGES = [
    "https://www.facebook.com/share/17Tbi8XFWq/?mibextid=wwXIfr",
    "https://www.facebook.com/share/1DiKxcSG4p/?mibextid=wwXIfr",
    "https://www.facebook.com/share/16eJnTqm5c/?mibextid=wwXIfr",
    "https://www.facebook.com/share/1HDHu2QxfE/?mibextid=wwXIfr"
]

def run():
    print("→ Bắt đầu quét 3 page Facebook...")

    urls = get_from_multiple_pages(PAGES, limit_each=100)

    print(f"→ Tổng video lấy được: {len(urls)}")

    new = filter_new_videos(urls)

    if not new:
        print("Không có video mới.")
        return
    
    print(f"→ Video mới: {len(new)}")

    processed = []

    for i, url in enumerate(new[:20]):
        raw = f"raw_{i}.mp4"
        out = f"edit_{i}.mp4"

        print(f"→ Tải: {url}")
        download(url, raw)

        print(f"→ Xử lý video {i}")
        process_video(raw, out)

        processed.append(out)

    print("→ Bắt đầu ghép đủ 30 phút...")
    build_30m(processed, "final.mp4")

    print("→ Tạo SEO Title + Mô tả...")
    title, desc = gen_title_desc()

    schedule = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).isoformat("T") + "Z"
    
    print("→ Upload YouTube...")
    upload("final.mp4", title, desc, schedule)

    db = load_db()
    db["used"] += new[:20]
    save_db(db)

    print("→ DONE!")
