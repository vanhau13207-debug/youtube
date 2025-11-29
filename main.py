from fb_scraper import get_reels_from_pages
from video_editor import process_video
from concat_builder import build_30m
from uploader import upload
from title_desc import gen_title_desc
from download import download
from db import load_db, save_db
import datetime, os

# ★★★ THÊM NHIỀU PAGE Ở ĐÂY ★★★
PAGES = [
    "https://www.facebook.com/profile.php?id=100091512082274&name=xhp_nt__fblite__profile__tab_bar&profile_tab_item_selected=reels",
    "https://www.facebook.com/profile.php?id=100092614194952&name=xhp_nt__fblite__profile__tab_bar&profile_tab_item_selected=reels",
    "https://www.facebook.com/profile.php?id=100084160534408&name=xhp_nt__fblite__profile__tab_bar&profile_tab_item_selected=reels",
    "https://www.facebook.com/profile.php?id=100090901622998&name=xhp_nt__fblite__profile__tab_bar&profile_tab_item_selected=reels",
    "https://www.facebook.com/musideshenguo.121/reels/",
    "https://www.facebook.com/profile.php?id=61559029680323&name=xhp_nt__fblite__profile__tab_bar&profile_tab_item_selected=reels"
]


def run():
    print("Đang quét nhiều page...")
    all_urls = get_reels_from_pages(PAGES, limit_each=40)

    db = load_db()
    new = [u for u in all_urls if u not in db["used"]]

    if not new:
        print("Không có video mới.")
        return

    print("Đã tìm thấy:", len(new), "video mới")

    processed = []

    for i, url in enumerate(new[:20]):  # lấy tối đa 20 video để ghép 30 phút
        raw = f"raw_{i}.mp4"
        out = f"edit_{i}.mp4"

        print("Tải video:", url)
        download(url, raw)

        print("Xử lý video...")
        process_video(raw, out)
        processed.append(out)

    print("Ghép video đủ 30 phút...")
    build_30m(processed, "final.mp4")

    print("Tạo tiêu đề + mô tả...")
    title, desc = gen_title_desc()

    print("Upload lên YouTube...")
    schedule = (datetime.datetime.utcnow() + datetime.timedelta(hours=3))\
        .isoformat("T") + "Z"
    upload("final.mp4", title, desc, schedule)

    # lưu video đã dùng
    db["used"] += new[:20]
    save_db(db)

    print("XONG.")
