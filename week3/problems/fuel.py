def main():
    while True:
        fraction_str = input("Fraction (X/Y): ")
        status = convert_to_percent(fraction_str)
        if status is not None:
            print(status)
            break

def convert_to_percent(fraction_str):
    try:
        num, denom = fraction_str.split("/")
        percent = (int(num) / int(denom)) * 100
        percent = round(percent)
        if percent <= 1:
            return "E"
        elif percent >= 99 and percent <= 100:
            return "F"
        elif percent < 99:
            return f"{percent}%"
    except (ValueError, ZeroDivisionError):
        pass

main()

# PASS
# check50 --local cs50/problems/2022/python/fuel