import requests
import re

def get_reels_from_page(page_url, limit=50):
    try:
        html = requests.get(page_url).text
    except:
        return []

    # lấy link video reels HD/FHD
    pattern = r'"browser_native_hd_url":"(.*?)"'
    urls = re.findall(pattern, html)

    # decode chuỗi escape
    urls = [u.encode().decode('unicode_escape') for u in urls]

    # lọc unique
    return list(dict.fromkeys(urls))[:limit]


def get_reels_from_pages(pages, limit_each=50):
    all_urls = []
    for page in pages:
        print(f"Đang quét page: {page}")
        urls = get_reels_from_page(page, limit_each)
        all_urls.extend(urls)

    # lọc unique toàn hệ thống
    all_urls = list(dict.fromkeys(all_urls))
    return all_urls
