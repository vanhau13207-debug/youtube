import requests

def get_reels_from_page(page_url):
    api = "https://fbdownloader.io/api/reels?url=" + page_url
    try:
        r = requests.get(api, timeout=15).json()
        if "video" in r and "hd" in r["video"]:
            return [r["video"]["hd"]]
        if "video" in r and "sd" in r["video"]:
            return [r["video"]["sd"]]
        return []
    except:
        return []
