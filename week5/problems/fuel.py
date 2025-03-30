def main():
    while True:
        fraction_str = input("Fraction (X/Y): ")
        status = convert(fraction_str)
        if status is not None:
            print(status)


def convert(fraction):
    num, denom = fraction.split("/")
    try:
        percent = (int(num) / int(denom)) * 100
        percent = round(percent)
        return gauge(percent)
    except (ValueError, ZeroDivisionError):
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    elif percentage <= 100:
        return f"{percentage}%"


if __name__ == "__main__":
    main()