def main():
    entrada = input("File name: ").strip().lower()
    file_name (entrada)


def file_name (x):
    if x.endswith(".gif"):
        print ("image/gif")

    elif x.endswith (".jpg") or x.endswith(".jpeg"):
        print ("image/jpeg")

    elif x.endswith (".png"):
        print ("image/png")

    elif x.endswith (".pdf"):
        print ("application/pdf")

    elif x.endswith (".txt"):
        print ("text/plain")

    elif x.endswith (".zip"):
        print ("application/zip")

    else:
        print ("application/octet-stream")

main()


