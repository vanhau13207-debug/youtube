import requests
import re

def get_reels_from_page(page_url, limit=50):
    html = requests.get(page_url).text
    pattern = r'"browser_native_hd_url":"(.*?)"'
    urls = re.findall(pattern, html)
    cleaned = [u.encode('utf-8').decode('unicode_escape') for u in urls]
    return list(dict.fromkeys(cleaned))[:limit]

def get_from_multiple_pages(pages, limit_each=50):
    all_videos = []
    for p in pages:
        print(f"Đang quét page: {p}")
        try:
            vids = get_reels_from_page(p, limit_each)
            all_videos.extend(vids)
        except:
            print(f"Lỗi khi quét page: {p}")
    return list(dict.fromkeys(all_videos))
