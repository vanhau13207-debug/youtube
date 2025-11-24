import ffmpeg

def process_video(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .hflip()
        .filter("setpts", "PTS/0.9")
        .filter("eq", contrast=1.05, saturation=1.1)
        .filter("pad", width=1080, height=1920, x="(ow-iw)/2", y="(oh-ih)/2", color="black")
        .drawtext(
            text="⚠️ DANGER - DO NOT COPY",
            fontcolor="red",
            fontsize=50,
            x="(w-text_w)/2",
            y="h-150",
            borderw=3,
        )
        .output(output_file, vcodec="libx264", acodec="aac", preset="fast")
        .overwrite_output()
        .run()
    )
