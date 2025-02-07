def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()
            print(convert(date, months))
            break
        except ValueError:
            pass

def convert(date, months):
    # Try parsing as mm/dd/yyyy
    try:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if m < 1 or m > 12 or d < 1 or d > 31:
            raise ValueError
        return f"{y}-{m:02}-{d:02}"


    except ValueError:

        if "," in date:
            parts = date.split(",")
            month_day = parts[0].strip().split(" ")
            if len(month_day) != 2:
                raise ValueError
            month_str, day_str = month_day
            month_str = month_str.strip().capitalize()
            day = int(day_str)
            if month_str not in months:
                raise ValueError
            month = months.index(month_str) + 1
            year = int(parts[1].strip())
            if day < 1 or day > 31 or month < 1 or month > 12:
                raise ValueError
            return f"{year}-{month:02}-{day:02}"

     
        raise ValueError

main()
