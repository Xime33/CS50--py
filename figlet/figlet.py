import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()  # Crear la instancia de Figlet
    fuentes_disponibles = figlet.getFonts()  # Obtener lista de fuentes

    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        fuente = sys.argv[2]
        if fuente not in fuentes_disponibles:  # Validar si la fuente existe
            print("Error: Fuente no disponible.")
            sys.exit(1)
    elif len(sys.argv) == 1:
        fuente = random.choice(fuentes_disponibles)  # Seleccionar fuente aleatoria
    else:
        sys.exit(1)

    respuesta = input("Input: ")

    figlet.setFont(font=fuente)  # Configurar la fuente seleccionada

    print("Output:")
    print(figlet.renderText(respuesta))  # Imprimir el texto en ASCII art

if __name__ == "__main__":
    main()
