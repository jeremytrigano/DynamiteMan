def initJoueurs():
    # choix du personnage
    choixPerso = 0
    choixAvatar = ""
    while True:
        try:
            print("Choisissez un personnage :", "1- ☺", "2- ☻", sep="\n")
            choixPerso = int(input())
            if choixPerso == 1 or choixPerso == 2:
                break
        except:
            continue
    if choixPerso == 1:
        choixAvatar = "☺"
    if choixPerso == 2:
        choixAvatar = "☻"

    # choix du nom du joueur
    choixNom = ""
    while isinstance(choixNom, str) and choixNom == "":
        if choixPerso == 1:
            print("Donnez un nom à votre personnage ☺:")
        if choixPerso == 2:
            print("Donnez un nom à votre personnage ☻:")
        choixNom = input()

    return (choixAvatar, choixNom)


def initCarte():
    carte = "carte"
    return carte

# test création joueur
joueur = initJoueurs()
print(f'{joueur[1]}, voici votre avatar {joueur[0]}')
# test création carte
print(initCarte())