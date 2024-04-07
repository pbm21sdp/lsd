#A2


import functools


#1


def grade(c):
    f = 1.8 * c + 32
    return f


print("Numarul de grade Fahrenheit este: " + str(grade(20)))
print("Numarul de grade Fahrenheit este: " + str(grade(100)))
print("Numarul de grade Fahrenheit este: " + str(grade(3)))

#2


def sumacifimp(n):
    if n <= 9:
        if n % 2 == 1:
            return n
        else:
            return "Numarul nu are cifre impare"
    else:
        ultimacif = n % 10
        if ultimacif % 2 == 1:
            return ultimacif + sumacifimp(n // 10)
        else:
            return sumacifimp(n // 10)


print("Suma cifrelor impare este: " + str(sumacifimp(12345)))
print("Suma cifrelor impare este: " + str(sumacifimp(12456)))
print("Suma cifrelor impare este: " + str(sumacifimp(24)))
print("Suma cifrelor impare este: " + str(sumacifimp(2)))
print("Suma cifrelor impare este: " + str(sumacifimp(5)))
print("Suma cifrelor impare este: " + str(sumacifimp(32135)))


#3
#Acest cod nu primeste o conditie predefinita


def prodelem(lista, cond):
    return functools.reduce(lambda a, b: a * b if cond(b) else a, lista, 1)


print("Produsul elementelor care respecta conditia este: " + str(prodelem([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)))
print("Produsul elementelor care respecta conditia este: " + str(prodelem([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 1)))

#Acest cod primeste o conditie predefinita


def cond1(x):
    if x % 2 == 0:
        return True
    else:
        return False


def prod(lista, cond1):
    return functools.reduce(lambda a, b: a * b if cond1(b) else a, lista, 1)


print("Produsul elementelor care respecta conditia este: " + str(prod([1, 2, 3, 4, 5, 6, 7, 8], cond1)))


