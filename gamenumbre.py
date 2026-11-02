import random

def jeu():
    secret = random.randint(1, 100)
    essais = 0

    print("===== JEU DEVINER LE NOMBRE =====")
    print("J'ai choisi un nombre entre 1 et 100")

    while True:
        n = int(input("Devinez le nombre : "))
        essais += 1

        if n < secret:
            print("Trop petit !")
        elif n > secret:
            print("Trop grand !")
        else:
            print("Bravo ! Vous avez gagne !")
            print("Nombre d'essais :", essais)
            break

jeu()
