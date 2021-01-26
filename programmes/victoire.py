def victoire(g,j):
    if horiz(g,j,l,c)==True or vertic(g,j,l,c)==True or diag(g,j,l,c)==True:
        print("le joueur ",j," a gagné.On peut tous sauter sur le vainqueur mais en fait non parce que c'est pas très covid mdr.")
        return True
    else:
        return False