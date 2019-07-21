import numpy as np

# liste assets graphiques
avatar1 = "☺"
avatar2 = "☻"
elMurPlein = "▓"
elSol = "░"
elDestruc = "▓"


def initJoueurs():
    # choix du personnage
    choixPerso = 0
    choixAvatar = ""
    while True:
        try:
            print("Choisissez un personnage :", f"1- {avatar1}", f"2- {avatar2}", sep="\n")
            choixPerso = int(input())
            if choixPerso == 1 or choixPerso == 2:
                break
        except:
            continue
    if choixPerso == 1:
        choixAvatar = avatar1
    if choixPerso == 2:
        choixAvatar = avatar2

    # choix du nom du joueur
    choixNom = ""
    while True:
        try:
            if choixPerso == 1:
                print(f"Donnez un nom à votre personnage {avatar1}:")
            if choixPerso == 2:
                print(f"Donnez un nom à votre personnage {avatar2}:")
            choixNom = input()
            if isinstance(choixNom, str) and choixNom != "":
                break
        except:
            continue

    return choixAvatar, choixNom


def initCarte():
    carte = np.full((15, 13), elDestruc, dtype='str')
    carte[1:-1:2, 1:-1] = elSol
    carte[1:-1, 1:-1:2] = elSol
    # partie normale
    nbDestruc = 60
    # partie rapide
    # nbDestruc = 10

    if nbDestruc == 60:
        carte[3, 5] = elDestruc
        carte[3, 6] = elDestruc
        carte[3, 7] = elDestruc
        carte[4, 3] = elDestruc
        carte[-2, 5] = elDestruc
        carte[-2, 6] = elDestruc
        carte[-2, 7] = elDestruc

    return carte

def afficheCarte(carte):
    if isinstance(joueur[0], str):
        carte[1, 1] = joueur[0]
    for ligne in carte:
        ligneCarte = ""
        for elem in ligne:
            ligneCarte += elem
        print(ligneCarte)

# création joueur
joueur = initJoueurs()
print(f'{joueur[1]}, voici votre avatar {joueur[0]}')
# création carte
carte = initCarte()

afficheCarte(carte)