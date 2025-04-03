import re

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        print(f"Error: {e}")

def convert(s):
    if matches := re.match(r'(\d{1,2}):?([0-5][0-9])?\s?(AM|PM)\s+to\s+(\d{1,2}):?([0-5][0-9])?\s?(AM|PM)', s, re.IGNORECASE):
        start_hour = int(matches.group(1))
        start_mins = int(matches.group(2)) if matches.group(2) else '00'
        start_is = matches.group(3)
        end_hour = int(matches.group(4))
        end_mins = int(matches.group(5)) if matches.group(5) else '00'
        end_is =  matches.group(6)

        start_24_hour = start_hour
        if str(start_is).lower() == "am" and start_hour == 12:
            start_24_hour = 0
        elif str(start_is).lower() == "pm" and start_hour != 12:
            start_24_hour = start_hour + 12

        end_24_hour = end_hour
        if str(end_is).lower() == "am" and end_hour == 12:
            end_24_hour = 0
        elif str(end_is).lower() == "pm" and end_hour != 12:
            end_24_hour = end_hour + 12

        start_24_time = f"{start_24_hour}:{start_mins}"
        end_24_time = f"{end_24_hour}:{end_mins}"

        return f"{start_24_time} to {end_24_time}"
    else:
        raise ValueError("Invalid")


if __name__ == "__main__":
    main()