"""
3. Implementați funcția standard filter care ia ca parametri o funcție booleană f și o mulțime s și
returnează mulțimea elementelor din s care satisfac funcția f.

Input: lambda x: x % 2 == 0, {1, 2, 3, 4}; Output: {2, 4}
"""

import functools


def filterset(f, a, b=set()):
    def functie(acc, elem):
        if f(elem):
            b.add(elem)
        return f(elem)
    functools.reduce(functie, a, 0)
    return b


def impar(x):
    return x % 2


b = set(filterset(impar, {1, 2, 3, 4, 5, 6}))
print("Elementele multimii care satisfac conditia sunt: " + str(b))

#Codul acesta nu este scris de mine, este luat din Cursul 5

"""
5. Scrieți o funcție care ia o lista de mulțimi (de exemplu, de șiruri), 
și returnează reuniunea (variantă: intersectia) mulțimilor.

Input: [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]; Output: reuniune: {1, 2, 3, 4, 5, 6, 7}; 
intersectie: {3}
"""
lista= [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]
def  reuniune(lista, multime=set(),n=0):
    if n<len(lista):
        multime.update(lista[n])
        return reuniune(lista,multime,n+1)
    return multime

def inters(lista,multime=lista[0],n=0):
    if n<len(lista):
        multime=multime.intersection(lista[n])
        return inters(lista,multime,n+1)
    return multime

print("Intersectia multimilor este: " + str(inters(lista)))
print ("Reuniunea multimilor este: " + str(reuniune(lista)))


"""
5. Implementați cu ajutorul lui reduce funcția map care construiește un dicționar în care toate valorile 
au fost transformate folosind o funcție dată ca parametru.
"""
dictionar={'a': 5, 'b': 7, 'c': 6}

def modificare(pereche, dictionar):
    cheie, valoare = pereche
    dictionar[cheie] = valoare+1
    return dictionar


def functiemap(dictionar):
    return functools.reduce(lambda dictionar_nou, pereche: modificare(pereche, dictionar_nou), dictionar.items(), {})


print("Dictionarul modificat este: " + str (functiemap(dictionar)))

"""
6. Scrieți o funcție care primește un dicționar de la șiruri la întregi și o listă de șiruri 
și returnează mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă.

Input: {'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']; Output: {5, 7}
"""

dictionar = {'aa': 5, 'bb': 7, 'ca': 6}
lista = ['aa', 'bb', 'c']

def ex6(dictionar, lista, dnou=[],n=0):
    if(n<len(lista)):
        if lista[n] in dictionar.keys():
            dnou.append(dictionar[lista[n]])
        return ex6(dictionar,lista,dnou,n+1)
    return dnou


print("Mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă este: " + str(ex6(dictionar, lista)))

