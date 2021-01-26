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
    print("\n")
    if j == 1:
        j=2
    else:
        j=1


def horiz(g, j, l, c):
    verif_j1 = 0
    verif_j2 = 0
    for c in range(5):
        for l in range(3):
            if g[l][c] == 1:
                verif_j2 = 0
                verif_j1 += 1
            if g[l][c] == 2:
                verif_j1 = 0
                verif_j2 += 1
            if g[l][c] == 0:
                verif_j2 = 0
                verif_j1 = 0
            if verif_j1 == 4:
                victoire(g, 1)
            if verif_j2 == 4:
                victoire(g, 2)


def vertic(g, j, l, c):
    verif_j1 = 0
    verif_j2 = 0
    for l in range(6):
        for c in range(2):
            if g[l][c] == 1:
                verif_j2 = 0
                verif_j1 += 1
            if g[l][c] == 2:
                verif_j1 = 0
                verif_j2 += 1
            if g[l][c] == 0:
                verif_j2 = 0
                verif_j1 = 0
            if verif_j1 == 4:
                victoire(g, 1)
            if verif_j2 == 4:
                victoire(g, 2)




def victoire(g,j):
    if horiz(g,j,l,c)==True or vertic(g,j,l,c)==True or diag(g,j,l,c)==True:
        print("le joueur ",j," a gagné. On peut tous sauter sur le vainqueur mais en fait non parce que c'est pas très covid mdr.")
        return True
    else:
        return False


def match_nul(g):
    for m in range(7):
        if g[0][m]==0:
            return False
    print("Match nul .Serrez vous la main mais en fait non parce que c'est pas très covid mdr.")
    return True


def coup_aleatoire(g, j):
    while True:
        c = random.randint(1,7)
        if coup_possible(g, c) == True:
            return c
        if match_nul(g) == True:
            return True






def jeufinalbot():
    grille_vide()
    affiche(g)
    j = random.randint(1,2)
    l = 0
    while True:
        if j == 2:
            coup_possible(g, c)
        else:
            coupaccepte=False
            while coupaccepte == False:
                c = int(input("Choisissez une colonne: "))
                if coup_possible(g, c) == True:
                    coupaccepte = True
        jouer(g, j, c)
        if match_nul(g) == True:
            affiche(g)
            print("\n")
            return "Match nul, rééssayez"
        if victoire(g, j) == True:
            affiche(g)
            if j == 2:
                return "Vous avez perdu"
            else:
                return "Vous avez gagné"
        
