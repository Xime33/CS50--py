
def main():
    while True:
          try:
                Fraction = input("Fraction: ")
                p = convert(Fraction)

                if p >= 99:
                      print(f"F")
                elif p <= 1:
                      print("E")
                else:
                     print(f"{convert(Fraction)}%")
                break
          except (ValueError, ZeroDivisionError):
                pass
def convert(input):
    x, y = input.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
            raise ZeroDivisionError
    if x > y:
            raise ValueError
    return round((x/y)*100)



main()
