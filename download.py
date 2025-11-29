import yt_dlp

def download(url, output):
    ydl_opts = {
        "outtmpl": output,
        "quiet": True,
        "format": "mp4/bestaudio/best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
