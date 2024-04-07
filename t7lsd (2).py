import functools


graf_neorientat = {1: [3], 2: [1, 3], 3: [2]}
g2 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
graf_orientat = {1: [2, 3], 2: [3], 3: [2, 1]}
graf1 = {1: [2], 2:[1, 3], 3:[1, 2]}


"""
6.Sa se scrie o functie care primeste ca parametru un graf neorientat si care determina daca este complet 
(returneaza True sau False). 
Într-un graf complet cu n vârfuri gradul fiecărui vârf este n-1, 
deoarece fiecare vârf este legat prin muchii de toate celelalte vârfuri.
"""


def grad(pereche, graf):
    n = len(list(graf.keys()))
    nod, lista_noduri_asociate = pereche
    gradul = len(lista_noduri_asociate)
    if gradul >= n-1:
        return True
    else:
        return False


def graf_complet(g):
    return functools.reduce(lambda exista, pereche_dictionar: True and exista if grad(pereche_dictionar, g)
                                                                              else False, g.items(), True)


print("Este graful complet? " + str(graf_complet(graf_neorientat)))
print("Este graful complet? " + str(graf_complet(g2)))

"""
7. Scrieti o functie care primeste ca parametru un graf orientat si doua numere (ce reprezinta noduri) 
si in cazul in care nu exista un arc de la primul nod la al doilea creeaza un astfel de arc, afiseaza noul graf 
si returneaza True. In cazul in care legatura exista deja inainte ca 
functia sa fie apelata, functia returneaza False.
"""


def arc(graf, n1, n2):
    if n2 in graf[n1]:
        return False
    else:
        graf[n1].append(n2)
        print(graf)
        return True


print(arc(graf_orientat, 1, 2))
print(arc(graf_orientat, 2, 1))
print(arc(graf1, 1, 3))
print(arc(graf1, 1, 2))
