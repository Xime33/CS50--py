import emoji

def main():

    respuesta = input("Input: ")
    print(emoji.emojize(f"Output: {respuesta}", language='alias'))



if __name__ == "__main__":
    main()
