def vertic(g, j, l, c):
    allignement = 0
    for i in range(6):
        if g[i][c] == j:
            allignement += 1
        else:
            allignement = 0
        if allignement == 4:
            return True
    return False

def horiz(g, j, l, c):
    allignement = 0
    for i in range(7):
        if g[l][i] == j:
            allignement += 1
        else:
            allignement = 0
        if allignement == 4:
            return True
    return False
    

