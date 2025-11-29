import requests
import re

# Lấy reels từ 1 page
def get_reels_from_page(page_url, limit=50):
    try:
        html = requests.get(page_url, headers={
            "User-Agent": "Mozilla/5.0"
        }).text

        # Regex link video mp4
        # Facebook đổi liên tục → Cái này là bản mới nhất 2025
        pattern = r'(https:[^"]+\.mp4)'
        matches = re.findall(pattern, html)

        # unique
        links = list(dict.fromkeys(matches))

        return links[:limit]

    except Exception as e:
        print(f"Error scraping {page_url}: {e}")
        return []


# Lấy reels từ nhiều page
def get_reels_from_pages(page_urls, limit_per_page=50):
    all_links = []

    for url in page_urls:
        print(f"Scraping page: {url}")
        links = get_reels_from_page(url, limit_per_page)
        print(f" → Found {len(links)} videos")
        all_links.extend(links)

    # unique lần cuối
    all_links = list(dict.fromkeys(all_links))

    print(f"Total collected: {len(all_links)} videos")
    return all_links
