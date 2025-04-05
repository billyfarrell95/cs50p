import emoji

def main():
    emoji_input = input("Input: ")
    print(emoji.emojize(emoji_input, language='alias'))

if __name__ == "__main__":
    main()

# PASS
# check50 --local cs50/problems/2022/python/emojize