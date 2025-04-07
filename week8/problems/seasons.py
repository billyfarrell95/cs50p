import datetime
import re, sys, inflect

def main():
    date = input("Date of Birth: ")
    if matches := re.match(r"^(\d{4})\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", date):
        year, month, day = int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
        today = datetime.date.today()
        today_dt = datetime.datetime(today.year, today.month, today.day)
        birthday_dt = datetime.datetime(year, month, day)
        p = inflect.engine()
        difference = minutes_since_date(today_dt, birthday_dt)
        print(f"{p.number_to_words(difference, andword="").capitalize()} {p.plural_noun('minute', difference)}")
    else:
        sys.exit("Invalid date")

def minutes_since_date(today_dt, birthday_dt):
    return round(((today_dt - birthday_dt).total_seconds()) / 60)

if __name__ == "__main__":
    main()