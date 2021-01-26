# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                 Pour jouer, appuyer sur le bouton start                   #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random
import time


def grille_vide():
    g=[[0 for i in range(7)]for j in range(6)]
    return g


def affiche(g):
    for i in range(6):
        ligne=""
        for j in range(7):
            if g[i][j] == 0:
                ligne+="I."
            if g[i][j] == 1:
                ligne+="Ix"
            if g[i][j] == 2:
                ligne+="Io"
        ligne+="I"
        print(ligne)
    return "\nAffichage terminé\n"


def coup_possible(g, c):
    veredict = False
    for i in range(5, -1, -1):
        if g[i][c] == 0:
            veredict = True
            return veredict
    return veredict


def jouer(g, j, c):
    tour_fini=0
    while tour_fini == 0:
        if coup_possible(g, c) == True:
            c-=1
            temp=0
            for l in range(6):
                if g[l][c] == 0:
                    g[l][c] = j
                    if temp != 0:
                        g[temp+-1][c] = 0
                    print("\n")
                    affiche(g)
                    time.sleep(0.3)
                temp+=1
            tour_fini=1
        else:
            c = int(input("Choisissez une colonne "))
    print("\n")
    if j == 1:
        j=2
    else:
        j=1














def jeufinalbot():
    grille_vide()
    affiche(g)
    c = int(input("Choisissez une colonne: "))
    j = 1
    