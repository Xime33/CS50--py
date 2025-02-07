def main():
    palabra = input ("Input: ")
    x = ''

    for char in palabra:
        if char not in 'aeiouAEIOU':
            x += char
    print(f"Output: {x}")

main()
