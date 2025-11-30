import requests
import re
import random
import time

# Fake user agents để tránh bị FB chặn
UA_LIST = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
]

def get_reels_from_page(url):
    headers = {"User-Agent": random.choice(UA_LIST)}
    
    try:
        res = requests.get(url, headers=headers, timeout=10)
        html = res.text

        # tìm link video fbcdn dạng .mp4
        pattern = r'https:\/\/video.*?\.mp4'
        matches = re.findall(pattern, html)

        return list(set(matches))  # remove duplicate

    except:
        return []

def get_reels_from_pages(list_pages):
    all_links = []

    for page in list_pages:
        print(f"\nĐang quét page: {page}")
        links = get_reels_from_page(page)
        print(f"  → Tìm được {len(links)} video")
        all_links.extend(links)

        time.sleep(random.uniform(1, 2))  # tránh bị block

    # unique
    all_links = list(set(all_links))
    return all_links
