cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"

nod1 = {cheie: 1, stanga: None, dreapta: None}  
nod7 = {cheie: 7, stanga: None, dreapta: None}  
nod4 = {cheie: 4, stanga: None, dreapta: None}  
nod5 = {cheie: 5, stanga: nod4, dreapta: nod7}
radacina = {cheie: 2, stanga: nod1, dreapta: nod5}  

print(radacina)


def afisare_inordine(arbore):
    if arbore is not None:   
        afisare_inordine(arbore[stanga])
        print(arbore[cheie], end=", ")
        afisare_inordine(arbore[dreapta])


print("\nafisare inordine: ", end="")
afisare_inordine(radacina)


def afisare_preordine(arbore):
    if arbore is not None:
        print(arbore[cheie], end=", ")
        afisare_preordine(arbore[stanga])
        afisare_preordine(arbore[dreapta])


print("\nafisare preordine: ", end="")
afisare_preordine(radacina)


def afisare_postordine(arbore):
    if arbore is not None:
        afisare_postordine(arbore[stanga])
        afisare_postordine(arbore[dreapta])
        print(arbore[cheie], end=", ")


print("\nafisare postordine: ", end="")
afisare_postordine(radacina)
