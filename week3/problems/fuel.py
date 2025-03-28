def main():
    while True:
        fraction_str = input("Fraction (X/Y): ")
        status = convert_to_percent(fraction_str)
        if status is not None:
            print(status)

def convert_to_percent(fraction_str):
    num, denom = fraction_str.split("/")
    try:
        percent = (int(num) / int(denom)) * 100
        percent = round(percent)
            
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if percent <= 1:
            return "E"
        elif percent >= 99 and percent <= 100:
            return "F"
        elif percent <= 100:
            return f"{percent}%"

main()