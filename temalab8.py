cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"


nod9 = {cheie: 9, stanga: None, dreapta: None}
nod3 = {cheie: 3, stanga: None, dreapta: None}
nod1 = {cheie: 1, stanga: None, dreapta: None}
nod7 = {cheie: 7, stanga: None, dreapta: nod9}
nod4 = {cheie: 4, stanga: nod3, dreapta: None}
nod5 = {cheie: 5, stanga: nod4, dreapta: nod7}
radacina = {cheie: 2, stanga: nod1, dreapta: nod5}  


def noduri_1_fiu(arbore):
    if arbore is not None:
        if (arbore[stanga] is None and arbore[dreapta] is not None) or (arbore[stanga] is not None and arbore[dreapta] is None):
            print (arbore[cheie])
        else:
            return noduri_1_fiu(arbore[stanga]) + noduri_1_fiu(arbore[dreapta])
    else:
        return 0


print("Numarul de noduri cu 1 singur fiu este: " + str(noduri_1_fiu(radacina)))


def nr_noduri(arbore):
    if arbore is not None:
        return 1 + nr_noduri(arbore[stanga]) + nr_noduri(arbore[dreapta])
    else:
        return 0


print("Numarul de noduri din arbore este: " + str(nr_noduri(radacina)))
