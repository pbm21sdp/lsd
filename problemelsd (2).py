"""
Exercițiul 9: Cerc
Implementați o funcție în Python care primește ca parametru raza unui cerc și
returnează atât lungimea discului cât și aria acestuia.
"""


pi = 3.14


def cerc(r):
    diametru = 2 * pi * r
    arie_disc = pi * r * r
    return diametru, arie_disc


"""
Exercițiul 10: Numărul de zile
Implementați o funcție în Python care primește ca parametri doi ani (numere întregi)
și returnează numărul de zile dintre aceștia (Puteți utiliza funcția implementată la exercițiul 4).
"""


def nr_zile(a, b):
    if a > b:
        dif1 = a - b
        z1 = dif1 / 4 * 366 + (dif1 - dif1 / 4) * 365
        return int(z1)
    else:
        dif2 = b - a
        z2 = dif2 / 4 * 366 + (dif2 - dif2 / 4) * 365
        return int(z2)
