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

