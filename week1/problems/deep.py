def main():
    name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    match name.lower().strip():
        case "42" | "forty-two" | "forty" | "forty two":
            print("Yes")
        case _:
            print("No")

main()