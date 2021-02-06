print ("\033[31mThis is red\033[0m")
g=[[0 for i in range(7)]for j in range(6)]
for i in range(6):
    ligne = ""
    for j in range(7):
        if g[i][j] == 0:
            ligne += "\033[34mI \033[0m"
        if g[i][j] == 1:
            ligne += "Ix"
        if g[i][j] == 2:
            ligne += "Io"
    ligne += "I"
    print(ligne)

'''
30: couleur noire
31: couleur rouge
32: couleur vert
33: couleur orange
34: couleur bleu
35: couleur violet
36: couleur turquoise
37: couleur blanc
'''