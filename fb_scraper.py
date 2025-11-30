import requests
import re

def load_cookie():
    raw = open("cookie.txt", "r").read().strip()
    cookies = {}
    for c in raw.split(";"):
        if "=" in c:
            k, v = c.strip().split("=", 1)
            cookies[k] = v
    return cookies

def get_reels_from_page(page_url):
    cookies = load_cookie()

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    r = requests.get(page_url, headers=headers, cookies=cookies)
    html = r.text

    # DEBUG: giúp bạn xem có đang bị redirect login không
    if "login" in html.lower() or "password" in html.lower():
        print("❌ Cookie die hoặc thiếu quyền → FB trả về trang login.")
        return []

    # Tìm link HD video gốc
    pattern = r'"browser_native_hd_url":"(.*?)"'
    found = re.findall(pattern, html)

    return [x.replace("\\/", "/") for x in found]
