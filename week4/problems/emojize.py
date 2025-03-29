import emoji

def main():
    while True:
        emoji_input = input("Input: ")
        print(emoji.emojize(emoji_input, language='alias'))

main()