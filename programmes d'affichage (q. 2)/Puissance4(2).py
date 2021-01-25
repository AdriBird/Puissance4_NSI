def rectangle(h, l, sym,sym2):
    for i in range(h):
        z=0
        for j in range(l):
            print(sym, end="")
            z+=1
            if z!=8:
                print(sym2, end="")


        print()


rectangle(6, 8, "I",".")



