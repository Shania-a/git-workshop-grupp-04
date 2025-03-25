import nellie, nikita, shania

nellie.hellonellie()
print(nellie)

nikita.hejnikita()
print(nikita)

shania.helloshania()
print(shania)

def favoritmat():
    mat = input("Ange vems favoritmat du vill veta: ")
    if mat == "nellie":
        nellie.food()
    elif mat == "nikita":
        nikita.foodbranchnikita()
    elif mat == "shania":
        shania.minfavoritmat()
    else:
        print("Felaktigt namn") 
        
favoritmat()