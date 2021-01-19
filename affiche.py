

def grille_vide(symbole):
    for i in range(6):
        print("I", end="")
        for j in range(8):
            print(symbole, end="I")
        print()

grille_vide(".")
