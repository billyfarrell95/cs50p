import re

def main():
    url = input("URL: ").strip()
    
    # username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    # (?:https?://) - the ?: tells the re to not capture this in group
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
        print(f"Username: {matches.group(1)}")

if __name__ == "__main__":
    main()