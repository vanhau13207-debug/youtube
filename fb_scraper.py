import requests
import re

def get_reels(page_url):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    html = requests.get(page_url, headers=headers).text

    # Pattern bắt link video fbcdn (link mp4 thật)
    pattern = r'(https:\/\/video.*?\.mp4.*?)"'
    matches = re.findall(pattern, html)

    urls = [m.replace("\\", "") for m in matches]
    return list(dict.fromkeys(urls))
