def main():
    user_input = input(":) and :( will be converted to emojis: ")
    converted_input = convert(user_input)
    print(converted_input)

def convert(user_input):
    converted = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return converted

main()

# PASS
# check50 --local cs50/problems/2022/python/faces