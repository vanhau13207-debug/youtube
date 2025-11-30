import requests
import re

def get_reels_from_page(page_url):
    try:
        html = requests.get(page_url, timeout=10).text
    except:
        print("   → Lỗi không tải được page")
        return []

    # Regex lấy link trực tiếp trong html FB
    pattern = r'(https:\/\/video\.fbcdn\.net\/[^\"]+)'  
    found = re.findall(pattern, html)

    # Unique + sạch
    videos = list(dict.fromkeys(found))

    print(f"  → Tìm được {len(videos)} video")
    return videos


def get_reels_from_pages(pages):
    all_videos = []
    for page in pages:
        print(f"\nĐang quét page: {page}")
        vids = get_reels_from_page(page)
        all_videos.extend(vids)
    return list(dict.fromkeys(all_videos))
