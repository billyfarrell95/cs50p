def main():
    print("Formats accepted are 24h: 07:33, 7:33, 12:23 | 12h: 7:30 am, 5:30 pm")
    time = input("What time is it? ")
    convert(time)


def convert(input_str):
    hour = None
    minutes = None
    is_12_hour = "am" in input_str or "pm" in input_str
    match is_12_hour:
        case True:
            print("12h detected...")
            # expects format 07:30 am or 1:00 pm
            input_str_list = input_str.split(" ")
            time = input_str_list[0]
            am_pm = input_str_list[1]
            hour = float(time.split(":")[0])
            minutes = float(time.split(":")[1])
            if minutes < 60 and hour <= 12:
                match am_pm:
                    case "am":
                        if ((hour == 7) or (hour == 8 and minutes == 0)):
                            print("breakfast time")
                    case "pm":
                        if ((hour == 12) or (hour == 1 and minutes == 0)):
                            print("lunch time")
                        elif ((hour == 6) or (hour == 7 and minutes == 0)):
                            print("dinner time")
            else:
                print("Enter a valid time")
        case False:
            print("24h detected...")
            # expects format 7:00, 07:45, 15:34
            hour = float(input_str.split(":")[0])
            minutes = float(input_str.split(":")[1])
            if (minutes < 60 and hour < 24) or (minutes == 0 and hour == 24):
                if ((hour == 7) or (hour == 8 and minutes == 0)):
                    print("breakfast time")
                elif ((hour == 12) or (hour == 13 and minutes == 0)):
                    print("lunch time")
                elif ((hour == 18) or (hour == 19 and minutes == 0)):
                    print("dinner time")
            else:
                print("Enter a valid time")
        case _:
            print("Formatting error")

if __name__ == "__main__":
    main()