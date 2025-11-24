import requests
import re

def get_reels_from_page(page_url, limit=50):
    html = requests.get(page_url).text
    pattern = r'"browser_native_hd_url":"(.*?)"'
    urls = re.findall(pattern, html)
    return list(dict.fromkeys(urls))[:limit]
