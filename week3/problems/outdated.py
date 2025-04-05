months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input("Date: ").strip()
            formatted_date = format_date(date)
            print(formatted_date)
            break
        except ValueError as e:
            print(e)


def format_date(date_string):
    if date_string[0].isalpha():
        try:
            month, day, year = date_string.split(" ")
            if "," not in day:
                raise ValueError("Invalid date format")
            day = day.replace(",", "")
            if 1 <= int(day) <= 31:
                for i in range(len(months)):
                    if months[i] == month.title():
                        month_index = months.index(month.lower().title()) + 1
                        return f"{year}-{str(month_index).zfill(2)}-{str(day).zfill(2)}"
            else:
                raise ValueError("Invalid date format")
                
        except ValueError:
            raise ValueError("Invalid date format")
    else:
        try:
            month, day, year = date_string.split("/")
            month = int(month)
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
            else:
                raise ValueError("Invalid month or day in date format")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

main()

# PASS
# check50 --local cs50/problems/2022/python/outdated