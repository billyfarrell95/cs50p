GROCERY_LIST = []
def main():  
    while True:
        try:
            item = input("")
            make_list(item)
        except EOFError:
            show_list()
            exit()


def make_list(list_item):
    formatted_item = list_item.strip().upper()
    global GROCERY_LIST
    GROCERY_LIST.append(formatted_item)

def show_list():
    output_list = list(set(GROCERY_LIST))
    output_list.sort()
    for item in output_list:
        num_of_item = GROCERY_LIST.count(item)
        print(f"{num_of_item} - {item}")

main()