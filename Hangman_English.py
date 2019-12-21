print("\nThis is the hangman game! The rules are simple: \n1.- The first player has to say the word to guess \n2.- The second player has to say a letter \n3.- If the second player has hit all the letters, he wins \n4.- If the second player has committed 8 failures, he loses \n")

palabra = input("Enter the word to guess: ")
palabra = palabra.lower()
palabra_lista = []
lista = []
fallos = 0

for l in palabra:
    lista.append("_")
    palabra_lista.append(l)

while palabra_lista != lista and fallos != 8:
    i = 0

    letra = input("Enter a letter: ")
    print(" ")

    if letra not in palabra:   
        fallos += 1

        if fallos == 8:
            print("You have lost!")
        
        else:
            print(lista)
            print("Failures: " + str(fallos))

    else:
        while i < len(palabra):
            if letra == palabra[i]:
                lista[i] = letra
            i = i + 1
        print(lista)
        print("Failures: " + str(fallos))
    
    print(" ")

if fallos != 8:
    print("You have won!")

xyz = 0

while xyz == 0:
    x = input("Press enter to exit: ")
    xyz = 1
