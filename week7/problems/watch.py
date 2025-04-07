import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.match(r'<iframe.*?src="(https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/([a-zA-z0-9_-]).+)".*?',s,):
        id = match.group(1).split("/")[-1]
        return f"https://youtu.be/{id}"
    return None

if __name__ == "__main__":
    main()