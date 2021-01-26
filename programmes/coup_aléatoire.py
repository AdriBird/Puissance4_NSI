import random

g=[[0 for i in range(7)]for j in range(6)]

def coup_possible(g, c):
    for i in range(5, -1, -1):
        if g[i][c] == 0:
            return True
    return False

def coup_aleatoire(g, j):
    while True:
        c = random.randint(1,7)
        if coup_possible(g, c) == True:
            return c
        if match_nul(g) == True:
            return True


    