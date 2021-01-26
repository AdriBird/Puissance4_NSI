g=[[0 for i in range(7)]for j in range(6)]

def coup_possible(g, c):
    veredict = False
    for i in range(5, -1, -1):
        if g[i][c] == 0:
            veredict = True
            return veredict
    return veredict
    
print(coup_possible(g, 0))