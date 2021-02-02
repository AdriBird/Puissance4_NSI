def vertic(g, j, l, c):
    verif_j1 = 0
    verif_j2 = 0
    for c in range(7):
        for l in range(6):
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
                return True
            if verif_j2 == 4:
                return True
    return False
            


def horiz(g, j, l, c):
    verif_j1 = 0
    verif_j2 = 0
    for l in range(6):
        for c in range(7):
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
                return True
            if verif_j2 == 4:
                return True



def diag(g, j, l, c):
    '''
    En gros il faut faire deux boucles: la grande boucle elle agit sur les lignes et la deuxième boucle
    agit sur les colonnes, si l'index des colonnes est inferieur à 3 elle va être croissante et si elle est
    supérieur à 3 elle est décroissante et si elle est égale à 3 elle est les deux
    '''
    verif_j = 0
    diag_verif = [0][0]
    if l < c:
        diag_verif = g[0][c-l]
        for i in range(len(g)-l):
            if diag_verif[i][(c-l)+i] !=0:
                verif_j += 1
            else:
                verif_j = 0
    else:
        diag_verif = g[l-c][0]
        for i in range(len(g)-l):
            if diag_verif[(l-c)+i][i] != 0:
                verif_j += 1
            else:
                verif_j = 0






g=[
[2, 1, 1, 1, 2, 2, 1,],
[2, 1, 2, 2, 1, 2, 1,],
[2, 1, 2, 1, 2, 1, 2,],
[2, 1, 2, 1, 2, 1, 2,],
[1, 2, 1, 2, 2, 1, 1,],
[1, 2, 2, 1, 1, 2, 2,],
]

print(horiz(g, 2, 3, 5))