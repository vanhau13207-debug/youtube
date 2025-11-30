import requests
import re

def get_reels_from_page(page_url, limit=50):
    """
    Lấy link reels từ 1 page
    """
    try:
        html = requests.get(page_url, timeout=15).text
    except:
        return []

    # Regex tìm link reel (HD + SD)
    patterns = [
        r'"browser_native_hd_url":"(.*?)"',
        r'"browser_native_sd_url":"(.*?)"'
    ]

    found = []
    for p in patterns:
        matches = re.findall(p, html)
        for m in matches:
            link = m.encode('utf-8').decode('unicode_escape')
            found.append(link)

    # Unique + limit
    found = list(dict.fromkeys(found))
    return found[:limit]


def get_reels_from_pages(page_urls, limit_each=30):
    """
    Lấy reels từ nhiều page
    """
    all_links = []

    for url in page_urls:
        print(f"Đang quét page: {url}")
        links = get_reels_from_page(url, limit_each)
        print(f"  → Tìm được {len(links)} video")
        all_links.extend(links)

    # Unique tất cả
    all_links = list(dict.fromkeys(all_links))
    return all_links
