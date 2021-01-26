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



def diag(g, j, l, c):
    '''
    En gros il faut faire deux boucles: la grande boucle elle agit sur les lignes et la deuxième boucle
    agit sur les colonnes, si l'index des colonnes est inferieur à 3 elle va être croissante et si elle est
    supérieur à 3 elle est décroissante et si elle est égale à 3 elle est les deux
    '''
    verif_j1 = 0
    verif_j2 = 0
    for i in range(5):
        for j in range(5):
            if g[j+i][j+i]
