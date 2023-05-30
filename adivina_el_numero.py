import random


def adivina_el_numero(x):

    print("====================")
    print("¡Bienvenido(a) al Juego!")
    print("====================")
    print("Tu meta es adivinar el número generado por el ordenador.")

    random_number = random.randint(1, x) #Número aleatorio entre 1 y x (a.i)

    prediction = 0
    while prediction != random_number:
        #El usuario añade un número
        prediction = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string

        if prediction < random_number:
            print("Intentalo otra vez. Este número es muy pequeño.")
        elif prediction > random_number:
            print("Intentalo otra vez. Este número es muy grande.")
    print(f"¡Felicidades! Has adivinado el número {random_number} correctamente.")


adivina_el_numero(100)