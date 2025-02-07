def main():
    # Ask the user for the input
    Q = input("What time is it? ")
    hours = convert(Q)  # Convert the time to hours as a float
    print(meal_time(hours))


def convert(time):

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)


    return hours + minutes / 60.0


def meal_time(hours):

    if 7 <= hours <= 8:
        return "breakfast time"
    elif 12 <= hours <= 13:
        return "lunch time"
    elif 18 <= hours <= 19:
        return "dinner time"
    return "" 


if __name__ == "__main__":
    main()
