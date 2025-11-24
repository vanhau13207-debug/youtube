import subprocess
import ffmpeg

def get_duration(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries",
         "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    ).decode())

def build_30m(videos, out):
    total = 0
    final = []

    for v in videos:
        d = get_duration(v)
        if total + d <= 1800:  # 30 phút
            total += d
            final.append(v)

    with open("concat.txt", "w") as f:
        for v in final:
            f.write(f"file '{v}'\n")

    ffmpeg.input("concat.txt", format="concat", safe=0)\
        .output(out, vcodec="libx264", acodec="aac")\
        .overwrite_output()\
        .run()
