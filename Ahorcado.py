print("\n ¡Este es el juego del ahorcado! Las normas son simples: \n 1.- El primer jugador tiene que decir la palabra a adivinar \n 2.- El segundo jugador tiene que decir una letra \n 3.- Si el segundo jugador ha acertado todas las letras, gana \n 4.- Si el segundo jugador ha cometido 8 fallos, pierde\n")

palabra = input("Introduce la palabra a adivinar: ")
palabra = palabra.lower()
palabra_lista = []
lista = []
fallos = 0

for l in palabra:
    lista.append("_")
    palabra_lista.append(l)

while palabra_lista != lista and fallos != 8:
    i = 0

    letra = input("Introduce una letra: ")
    print(" ")

    if letra not in palabra:   
        fallos += 1

        if fallos == 8:
            print("¡Has perdido!")
        
        else:
            print(lista)
            print("Fallos: " + str(fallos))

    else:
        while i < len(palabra):
            if letra == palabra[i]:
                lista[i] = letra
            i = i + 1
        print(lista)
        print("Fallos: " + str(fallos))
    
    print(" ")

if fallos != 8:
    print("¡Has ganado!")