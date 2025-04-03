import re

def main():
    print(count(input("Text: ")))

def count(s):
    if matches := re.findall(r'\bum\b', s.lower()):
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()