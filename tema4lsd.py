import functools

"""

3. a) Implementați funcția nth care returnează al n-lea element dintr-o listă.
b) Implementați o funcție firstn care returnează o listă cu primele n elemente dintr-o listă dată.

"""

"3. a)"


lista = [6, 4, 8, 10, 12, 13]


def nth(n, lista):
    print(lista[n])


print("Elementul n din lista: ")
nth(2, lista)

"3. b)"


def firstn(n, lista):

    print(lista[0:n])


print("Primele n elemente din lista sunt: ")
firstn(3, lista)

"""
6. a) Implementați folosind reduce o funcție countif care ia ca parametru o funcție f cu valori boolene și o listă și 
returnează numărul de elemente pentru care funcția f e adevărată.
b) Implementați similar o funcție sumif care calculează suma tuturor elementelor (presupuse întregi) 
pentru care funcția f e adevărată.
"""


def f(x):
    if x % 2 == 0:
        return True
    else:
        return False


def countif(lista, f):
    return functools.reduce(lambda acc, element: acc + 1 if f(element) else acc, lista, 0)


print("Numarul de elemente pentru care functia f este adevarata este: ")
print(countif([1, 2, 3, 4, 6], f))

"6. b)"


def sumif(lista, f):
    return functools.reduce(lambda acc, element: element + acc if f(element) else acc, lista, 0)


print("Suma elementelor pentru care functia f este adevarata este: ")
print(sumif([1, 2, 3, 4, 5, 6, 7], f))


"""
9. Scrieți o funcție care ia o listă de cifre și returnează valoarea numărului cu cifrele respective.

"""


def cond(x):
    x = list[0]
    if x != 0:
        return True
    else:
        return False


def create_nr(lista, cond):
    if len(lista) > 0:
        head = lista[-1]
        tail = lista[:-1]
        if cond(head):
            return head + create_nr(tail, cond)*10
        else:
            return create_nr(tail, cond)
    else:
        return 0


"""
Acest cod de la ex 9 nu este scris in totalitate de mine, eu doar am modificat conditia 

"""

print("Numarul format cu aceste cifre este: ")
print(create_nr([0, 1, 2, 3, 0, 4], cond))
