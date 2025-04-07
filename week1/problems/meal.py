import sys

def main():
    time_input = input("What time is it? ")
    time = convert(time_input)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        sys.exit()

def convert(input_str):
    hour = float(input_str.split(":")[0])
    minutes = float(input_str.split(":")[1])
    time_int = hour + (minutes / 60)
    return time_int

if __name__ == "__main__":
    main()