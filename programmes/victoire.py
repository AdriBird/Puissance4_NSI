def victoire(g,j):
    if horiz(g,j,l,c)==True or vertic(g,j,l,c)==True or diag(g,j,l,c)==True:
        return True
    else:
        return False