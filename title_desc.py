import google.generativeai as gen
import os

gen.configure(api_key=os.getenv("GEMINI_API_KEY"))

TITLE_PROMPT = """
Generate an SEO-optimized YouTube title (max 65 chars) for a 9:16 dangerous stunt compilation.
Include words like “Do Not Try”, “Dangerous”, “Warning”.
"""

DESC_PROMPT = """
Write an SEO YouTube description (<900 chars) for a dangerous 9:16 Reels compilation.
Start with WARNING, include disclaimer, add 5-10 hashtags.
"""

def gen_title_desc():
    model = gen.GenerativeModel("gemini-1.5-flash")
    title = model.generate_content(TITLE_PROMPT).text
    desc = model.generate_content(DESC_PROMPT).text
    return title, desc
