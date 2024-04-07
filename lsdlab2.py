"""
Exercițiul 2: mediana
Scrieți o funcție care calculează mediana a trei valori (valoarea aflată între celelalte două).
Încercați să scrieți cod cât mai simplu, și să nu-l repetați.
Puteți folosi o funcție auxiliară care calculează mediana a trei numere,
pentru care știm că primul e mai mic sau egal decât al doilea.
Sau puteți încerca să compuneți doar funcțiile standard max/min de două elemente
(expresia trebuie să fie oarecum simetrică).
Care din variante necesită mai puține comparații?

"""


def media(a, b, c):
    maxim = max(max(a, b), c)
    minim = min(min(a, b), c)
    mediana = a + b + c - maxim - minim

    return mediana


"""
Codul acesta nu este scris de mine, a fost scris la laborator, am modificat doar ce afiseaza.

"""


"""
Exercițiul 3: operații cu funcții
În matematică, am extins uneori operatorul + de la numere la funcții, 
definind funcția f + g prin relația (f + g)(x) = f(x) + g(x)
a) Definiți o funcție care ia ca parametru două funcții f și g 
și returnează funcția definită ca suma lor prin relația de mai sus.
b) Scrieți o funcție mai generală, care primește ca parametru și operatorul binar 
(o funcție de două argumente) care e aplicată celor două funcții. 
Verificați că o puteți folosi cu operator.add și operator.sub pentru a calcula suma și diferența, 
dar încercați și alți operatori.

"""


def f(x):
    return x + 5


def g(x):
    return x + 10


"""
Am definit cele 2 functii pentru a verifica daca functia scrisa functioneaza corect.
"""


def fg(x):
    return f(x) + g(x)


import operator


def aplica_operator(operator, f, g):
    return operator(f, g)


"""
Exercițiul 4: functie anonima
Scrieti o funcție anonima care adaugă 15 la un număr dat ca argument.

"""


def h(x):
    return (lambda x: x + 15)(x)


"""
Codul acesta nu a fost scris de mine, a fost scris la laborator, eu am modificat valoarea adaugata lui x
"""