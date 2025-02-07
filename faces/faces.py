
def convert(texto):
    return texto.replace(":)","🙂").replace(":(","🙁")

def main():
    respuesta = input()
    print(convert(respuesta))

main()


