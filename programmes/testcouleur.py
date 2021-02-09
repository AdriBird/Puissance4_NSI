print ("\033[1;37;48mtest police")

print("\033[2;37;48mtest police")
g=[[0 for i in range(7)]for j in range(6)]

print('''
.______    __    __   __       _______.     _______.     ___      .__   __.   ______  _______     _  _    
|   _  \  |  |  |  | |  |     /       |    /       |    /   \     |  \ |  |  /      ||   ____|   | || |   
|  |_)  | |  |  |  | |  |    |   (----`   |   (----`   /  ^  \    |   \|  | |  ,----'|  |__      | || |_  
|   ___/  |  |  |  | |  |     \   \        \   \      /  /_\  \   |  . `  | |  |     |   __|     |__   _| 
|  |      |  `--'  | |  | .----)   |   .----)   |    /  _____  \  |  |\   | |  `----.|  |____       | |   
| _|       \______/  |__| |_______/    |_______/    /__/     \__\ |__| \__|  \______||_______|      |_|    
                                                                                                                              
''')

for i in range(6):
    ligne = ""
    for j in range(7):
        if g[i][j] == 0:
            ligne += "\033[1;37;48mI "
        if g[i][j] == 1:
            ligne += "\033[1;37;48mI\033[1;33;48m•"
        if g[i][j] == 2:
            ligne += "\033[1;37;48mI\033[1;31;48m•"
    ligne += "\033[1;37;48mI"
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