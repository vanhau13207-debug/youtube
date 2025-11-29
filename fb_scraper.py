import requests
import re

def get_reels_from_page(page_url):
    try:
        html = requests.get(page_url, timeout=10).text
    except:
        return []

    # link dạng browser_native_hd_url
    pattern = r'"browser_native_hd_url":"(.*?)"'
    urls = re.findall(pattern, html)

    # decode URL từ dạng escaped
    urls = [u.encode('utf-8').decode('unicode_escape') for u in urls]

    return list(dict.fromkeys(urls))  # unique


def get_reels_from_pages(list_pages):
    all_urls = []
    for page in list_pages:
        urls = get_reels_from_page(page)
        all_urls.extend(urls)

    # bỏ trùng lặp
    return list(dict.fromkeys(all_urls))
