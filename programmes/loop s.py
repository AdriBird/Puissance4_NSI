# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                           #
#              Adrien Cazin    Léon Gard    Matthieu Gautherot              #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random
import time


def grille_vide():
    '''
Fonction qui renvoie un tableau g à 2 dimensions plein de 0
'''
    g=[[0 for i in range(7)]for j in range(6)]
    return g


def affiche(g):
    '''
    Fonction qui prend en argument la grille
    et choisit l'affichage des pions en fonction du joueur.
    '''
    for k in range(7):
        print("", k+1, end="")
    print()
    for i in range(6):
        ligne=""
        for j in range(7):
            if g[i][j] == 0:
                ligne+="\033[1;37;48mI "
            if g[i][j] == 1:
                ligne+="\033[1;37;48mI\033[1;33;48m•"
            if g[i][j] == 2:
                ligne+="\033[1;37;48mI\033[1;31;48m•"
        ligne+="\033[1;37;48mI"
        print(ligne)
    return "\nAffichage terminé\n"


def coup_possible(g, c):
    '''
    Fonction qui prend en argument la grille et la colonne choisie
    et renvoie True s'il y a de l'espace dans la colonne, sinon elle renvoie False.
    '''
    c -= 1
    for i in range(5, -1, -1):
        if g[i][c] == 0:
            return True
    return False

g=[
[0, 0, 0, 0, 0, 0, 1,],
[0, 0, 0, 0, 0, 0, 1,],
[0, 0, 0, 0, 0, 0, 1,],
[0, 0, 0, 0, 1, 0, 1,],
[0, 0, 0, 0, 1, 0, 1,],
[0, 0, 0, 1, 1, 1, 1,],
]
assert coup_possible(g,7)==False
assert coup_possible(g,5)==True
assert coup_possible(g,1)==True


def jouer(g, j, c, anim):
    '''
    Fonction qui prend en argument la grille, le joueur et la colonne choisie
    et qui fait jouer un coup à ce joueur, en modifiant la grille g et affichant une animation de chute.
    '''    
    tour_fini=0
    ligne = -1
    while tour_fini == 0:
        if coup_possible(g, c) == True:
            c-=1
            temp=0
            for l in range(6):
                if g[l][c] == 0:
                    ligne += 1
                    g[l][c] = j
                    if temp != 0:
                        g[temp+-1][c] = 0
                    if anim == 1:
                        print("\n")
                        affiche(g)
                temp+=1
            tour_fini=1
            if anim == 0:
                print("\n")
                affiche(g)
    if j == 1:
        j = 2
    else:
        j = 1
    return ligne


def vertic(g, j, l, c):
    '''
    Fonction qui prend en argumentla grille et le joueur qui joue et vérifie dans tout le tableau
    s'il y a 4 symboles identiques alignés à la verticale et renvoie True si c'est le cas, sinon False.
    '''
    allignement = 0
    for i in range(6):
        if g[i][c] == j:
            allignement += 1
        else:
            allignement = 0
        if allignement == 4:
            return True
    return False

g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 1, 0, 0, 0, 0, 0,],
[0, 1, 0, 0, 0, 0, 0,],
[0, 1, 0, 0, 0, 0, 0,],
[0, 1, 0, 1, 1, 1, 1,],
]
assert vertic(g, 1, 1, 1) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 1, 1,],
[0, 0, 0, 2, 2, 2, 1,],
[0, 0, 0, 2, 1, 1, 1,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert vertic(g, 1, 2, 6) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 2, 1, 1,],
[0, 0, 0, 2, 2, 2, 1,],
[0, 0, 0, 2, 1, 1, 2,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert vertic(g, 1, 2, 6) == False


def horiz(g, j, l, c):
    '''
    Fonction qui prend en argument la grille et le joueur qui joue et vérifie dans tout le tableau 
    s'il y a 4 symboles identiques alignés à l'horizontale et renvoie True si c'est le cas, sinon False.
    '''
    allignement = 0
    for i in range(7):
        if g[l][i] == j:
            allignement += 1
        else:
            allignement = 0
        if allignement == 4:
            return True
    return False

g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 1, 1,],
]
assert horiz(g, 1, 5, 1) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 1, 1,],
[0, 0, 0, 2, 2, 2, 1,],
[0, 0, 0, 2, 1, 1, 2,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert horiz(g, 1, 2, 1) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 2, 1, 1,],
[0, 0, 0, 2, 2, 2, 1,],
[0, 0, 0, 2, 1, 1, 2,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert horiz(g, 1, 2, 1) == False



def diag(g, j, l, c):
    allignement = 0
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0 and ccopie <= 6 and ccopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie += 1
            ccopie += 1
        else:
            break
    allignement -= 1
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0 and ccopie <= 6 and ccopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie -= 1
            ccopie -= 1
        else:
            break
    if allignement >= 4:
        return True
    allignement = 0
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0 and ccopie <= 6 and ccopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie += 1
            ccopie -= 1
        else:
            break
    allignement -= 1
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0 and ccopie <= 6 and ccopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie -= 1
            ccopie += 1
        else:
            break
    if allignement >= 4:
        return True
    return False

g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 1, 0, 0, 1, 0, 0,],
[0, 1, 1, 1, 2, 0, 0,],
[0, 2, 1, 2, 1, 0, 0,],
[0, 1, 1, 2, 1, 1, 1,],
]
assert diag(g, 1, 3, 3) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 1, 1,],
[0, 0, 0, 2, 1, 2, 1,],
[0, 0, 0, 2, 1, 1, 1,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert diag(g, 1, 2, 3) == True
g=[
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 1, 2, 1, 1,],
[0, 0, 0, 2, 2, 2, 1,],
[0, 0, 0, 2, 1, 1, 2,],
[0, 0, 0, 2, 1, 2, 1,],
]
assert diag(g, 1, 2, 3) == False


def victoire(g, j):
    '''
    Fonction qui renvoie un booléen si un joueur a gagné.
    '''
    if j == 1:
        gagnant = "\033[1;33;48mjaune"
    if j == 2:
        gagnant = "\033[1;31;48mrouge"
    print("le joueur ",gagnant," \033[1;37;48ma gagné.\n ")
    #affiche(g)
    return True


def match_nul(g):
    '''
    Fonction qui prend en argument la grille
    et renvoie True s'il y a un match nul.
    '''
    for m in range(7):
        if g[0][m]==0:
            return False
    return True

g=[[1 for i in range(7)]for j in range(6)]
#assert match_nul(g) == True


def coup_aleatoire(g, j):
    '''
    Fonction qui prend en argument la grille et le joueur qui joue
    et choisit une colonne aléatoire pour que le bot la joue.
    '''
    while True:
        c = random.randint(0, 6)
        if coup_possible(g, c) == True:
            return c
        if match_nul(g) == True:
            return True






def jeufinalbot():
    victoiresrouges = 0
    victoiresjaunes = 0
    nbjouers=int(input("\033[1;37;48mJouer contre un bot (1); Jouer à deux (2): "))
    animations=int(input("(Beta) Activer animations? Oui (1); Non (0): "))
    parties = int(input("Combien de parties voulez vous jouer? "))
    for i in range(parties):
        g=grille_vide()
        match_fini = 0
        c = 0
        affiche(g)
        j = random.randint(1,2)
        while match_fini == 0:
            if nbjouers == 1:
                if j == 2:
                    c=coup_aleatoire(g, j)
                else:
                    coupaccepte=False
                    while coupaccepte == False:
                        c = int(input("Choisissez une colonne entre 1 et 7: "))
                        if c >= 1 and c <= 7:
                            if coup_possible(g, c) == True:
                                coupaccepte = True
            if nbjouers == 2:
                coupaccepte=False
                while coupaccepte == False:
                    c = int(input("Choisissez une colonne entre 1 et 7: "))
                    if c >= 1 and c <= 7:
                        if coup_possible(g, c) == True:
                            coupaccepte = True
            if nbjouers == 0:
                c=coup_aleatoire(g, j)
            l = jouer(g, j, c, animations)
            c -= 1
            if horiz(g, j, l, c) == True or vertic(g, j, l, c) == True or diag(g, j, l, c) == True:
                victoire(g, j)
                match_fini = True
            if match_nul(g) == True and match_fini == False:
                print("Match nul. \n")
                print("\n")
                match_fini = True
            if j == 1:
                j = 2
                if match_fini == True and match_nul(g) == False:
                    victoiresjaunes += 1
            else:
                j = 1
                if match_fini == True and match_nul(g) == False:
                    victoiresrouges += 1
    print("Le joueur rouge a gagné ", victoiresrouges, " fois")
    print("Le joueur jaune a gagné ", victoiresjaunes, " fois")
jeufinalbot()
        
