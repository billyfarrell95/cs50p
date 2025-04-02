import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'(?<=src=")(.*?)(?=[?"])', s):
        url = matches.group(1)
        if "youtube" in url:
            match_id = re.search(r'^(?:https?://)?(?:www\.)?youtube\.com/embed/([a-z0-9_].+)', url)
            video_id = match_id.group(1)
            short_url = f"https://youtu.be/{video_id}"
            return short_url



if __name__ == "__main__":
    main()