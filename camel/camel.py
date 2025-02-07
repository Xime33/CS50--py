def main():
    camelCase = input("camelCase: ")
    print(f"snake_case: {convert(camelCase)}")

def convert(camelCase):
    x = ''
    for char in camelCase:
        if char.isupper():
            x += "_" + char.lower()
        else:
            x += char
    return x



main()
