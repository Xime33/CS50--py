import inflect
nombres = []
p = inflect.engine()
while True:
    try:
        x = input("Name: ")
        nombres.append(x)
    except EOFError:
        print()
        break
print(f"Adieu, adieu, to "+ p.join(nombres))

