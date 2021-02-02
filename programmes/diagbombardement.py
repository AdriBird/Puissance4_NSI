


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
            if g[i][(c-l)+i] !=0:
                verif_j += 1
            if verif_j == 4:
                return True
            else:
                verif_j = 0
    else:
        diag_verif = g[l-c][0]
        for i in range(len(g)-l):
            if g[(l-c)+i][i] != 0:
                verif_j += 1
            if diag_verif == 4:
                return True
            else:
                verif_j = 0
    return False






g=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 2, 0],
[1, 1, 2, 0, 2, 0, 0],
[1, 1, 1, 2, 0, 0, 0],
[2, 2, 2, 1, 0, 2, 2],
]





def diagonale(g, j, l, c):
    allignement = 0
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie += 1
            ccopie += 1
        else:
            break
    allignement -= 1
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0:
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
    while lcopie <= 5 and lcopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie += 1
            ccopie -= 1
        else:
            break
    allignement -= 1
    lcopie = l 
    ccopie = c 
    while lcopie <= 5 and lcopie >= 0:
        if g[lcopie][ccopie] == j:
            allignement += 1
            lcopie -= 1
            ccopie += 1
        else:
            break
    if allignement >= 4:
        return True
    return False




print(diagonale(g, 1, 3, 1))