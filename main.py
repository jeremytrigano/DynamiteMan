import numpy as np

from pynput import keyboard
from time import sleep

import os
clear = lambda: os.system('cls')

global keyCapture
keyCapture = -1

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

    # avatar choisi, pseudo, coord y ligne, coord x colonne
    return {"avatar": choixAvatar,
            "pseudo": choixNom,
            "y": 1,
            "x": 1}


def initCarte(tJoueur):
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

    # positionnement des joueurs
    if isinstance(tJoueur["avatar"], str):
        carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]
    else:
        carte[tJoueur["y"], tJoueur["x"]] = "1"

    return carte

def afficheCarte(carte):
    for ligne in carte:
        ligneCarte = ""
        for elem in ligne:
            ligneCarte += elem
        print(ligneCarte)

def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    if key == keyboard.Key.up:
        carte[tJoueur["y"], tJoueur["x"]] = elSol
        tJoueur["y"] -= 1
        carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]

    clear()
    afficheCarte(carte)


tJoueur = initJoueurs()
print(f'{tJoueur["pseudo"]}, voici votre avatar {"tJoueur[avatar]"}')

carte = initCarte(tJoueur)

afficheCarte(carte)

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    sleep(0.25)