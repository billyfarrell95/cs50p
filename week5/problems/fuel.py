def main():
    fraction_str = input("Fraction (X/Y): ")
    status = convert(fraction_str)
    print(gauge(status))

def convert(fraction):
    try:
        num, denom = fraction.split('/')
        num, denom = int(num), int(denom)
        if denom == 0:
            raise ZeroDivisionError
        if num > denom:
            raise ValueError
        return round((num / denom) * 100)
    except (ValueError):
        raise ValueError("Invalid")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    elif percentage <= 100:
        return f"{percentage}%"

if __name__ == "__main__":
    main()