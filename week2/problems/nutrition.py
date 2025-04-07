from fruit_data import fruit_data
def main():
    item = input("Item: ")
    info = get_calories(item.lower().strip())
    print(info)

def get_calories(s):
    formatted_s = s.replace(" ", "_")
    try:
        return f"{fruit_data[f"{formatted_s}"]['calories']}"
    except:
        return ""

main()