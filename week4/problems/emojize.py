import emoji

def main():
    emoji_input = input("Input: ")
    print(emoji.emojize(emoji_input, language='alias'))

if __name__ == "__main__":
    main()