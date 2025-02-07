def main():
    diccionario = {}
    total = 0

    while True:
        try:
            x = input().upper()
            if x in diccionario:
                diccionario[x] += 1
            else:
                diccionario[x] = 1

        except EOFError:

            for i in sorted(diccionario.keys()):
                print(diccionario[i],i)

            break



main()
