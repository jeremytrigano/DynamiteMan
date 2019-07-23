import numpy as np

import pygame
from pygame.locals import *

# taille carte
nbLigne = 15
nbCol = 13


pygame.init()
fenetre = pygame.display.set_mode((40*17, 40*15), RESIZABLE)

fond = pygame.image.load("background.jpg").convert()
fond = pygame.transform.scale(fond, (40*17, 40*15))

# liste assets graphiques
elMurPlein = pygame.image.load("elMurPlein.png").convert()
elSol = pygame.image.load("elSol.png").convert()
elTemp = pygame.image.load("elSol.png").convert()
elNext = pygame.image.load("elSol.png").convert()
elDestruc = pygame.image.load("elDestruc.png").convert()
dynamite = pygame.image.load("dynamite.png").convert_alpha()
avatar1 = pygame.image.load("avatar1.png").convert_alpha()
avatar2 = pygame.image.load("avatar2.png").convert_alpha()

fenetre.blit(fond, (0, 0))


def initJoueurs():
    # choix du personnage
    choixPerso = 0
    choixAvatar = ""
    while True:
        try:
            print("Choisissez un personnage :", f"1- Rouge", f"2- Bleu", sep="\n")
            choixPerso = input()

            # par défaut
            if choixPerso == "":
                choixPerso = 1
            choixPerso = int(choixPerso)
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
            print(f"Donnez un nom à votre personnage :")
            choixNom = input()
            if choixNom == "":
                choixNom = "Tatatetetititototututyty"
            if isinstance(choixNom, str) and choixNom != "":
                break
        except:
            continue

    # avatar choisi, pseudo, coord y ligne, coord x colonne
    return {"avatar": choixAvatar,
            "pseudo": choixNom,
            "y": 1,
            "x": 1}


def initCarte():
    carte = np.full((nbLigne, nbCol), elMurPlein)
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

def initEmplJoueur(carte, tJoueur):
    # positionnement des joueurs
    carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]
    return carte

def afficheCarte(carte):
    i = 1
    for ligne in carte:
        j = 1
        for elem in ligne:
            fenetre.blit(elem, (i*40, j*40))
            j += 1
        i += 1
    pygame.display.flip()

def valideMvt(key):
    result = False
    if key == K_RETURN:
        result = True
    if key == K_LEFT and (carte[(tJoueur["y"]-1)%nbLigne, tJoueur["x"]] != elMurPlein and carte[(tJoueur["y"]-1)%nbLigne, tJoueur["x"]] != elDestruc):
        result = True
    if key == K_RIGHT and (carte[(tJoueur["y"]+1)%nbLigne, tJoueur["x"]] != elMurPlein and carte[(tJoueur["y"]+1)%nbLigne, tJoueur["x"]] != elDestruc):
        result = True
    if key == K_UP and (carte[tJoueur["y"], (tJoueur["x"]-1)%nbCol] != elMurPlein and carte[tJoueur["y"], (tJoueur["x"]-1)%nbCol] != elDestruc):
        result = True
    if key == K_DOWN and (carte[tJoueur["y"], (tJoueur["x"]+1)%nbCol] != elMurPlein and carte[tJoueur["y"], (tJoueur["x"]+1)%nbCol] != elDestruc):
        result = True

    pygame.display.flip()

    return result

tJoueur = initJoueurs()

carte = initCarte()
pygame.display.flip()
carte = initEmplJoueur(carte, tJoueur)
pygame.display.flip()


continuer = True
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                carte[tJoueur["y"], tJoueur["x"]] = dynamite
                elNext = dynamite
            if valideMvt(event.key):
                if event.key == K_LEFT:
                    elTemp = carte[tJoueur["y"]-1, tJoueur["x"]]
                    carte[tJoueur["y"], tJoueur["x"]] = elNext
                    elNext = elTemp
                    tJoueur["y"] -= 1
                    tJoueur["y"] = tJoueur["y"]%nbLigne
                    carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]
                if event.key == K_RIGHT:
                    elTemp = carte[tJoueur["y"]+1, tJoueur["x"]]
                    carte[tJoueur["y"], tJoueur["x"]] = elNext
                    elNext = elTemp
                    tJoueur["y"] += 1
                    tJoueur["y"] = tJoueur["y"] % nbLigne
                    carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]
                if event.key == K_UP:
                    elTemp = carte[tJoueur["y"], tJoueur["x"]-1]
                    carte[tJoueur["y"], tJoueur["x"]] = elNext
                    elNext = elTemp
                    tJoueur["x"] -= 1
                    tJoueur["x"] = tJoueur["x"] % nbCol
                    carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]
                if event.key == K_DOWN:
                    elTemp = carte[tJoueur["y"], tJoueur["x"]+1]
                    carte[tJoueur["y"], tJoueur["x"]] = elNext
                    elNext = elTemp
                    tJoueur["x"] += 1
                    tJoueur["x"] = tJoueur["x"] % nbCol
                    carte[tJoueur["y"], tJoueur["x"]] = tJoueur["avatar"]

        afficheCarte(carte)

