#     LAB 1

# Ex 1

def ultima(n):
    n = n % 10
    return n

print(ultima(34))


# Ex 2

def atomi(c, h, o):
    masa = c * 12 + h * 1 + o * 16
    return masa

print(atomi(2, 3, 5))


# Ex 3

import math

def ecuatie(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "ecuatia nu are sol reale"
    else:
        d = math.sqrt(delta)
        s1 = (-b + d)/(2 * a)
        s2 = (-b - d)/(2 * a)
        return s1, s2

#Ex4

def bisect(w):
    if w % 4 == 0:
        if w % 100 == 0:
            if w % 400 == 0:
                return True
            else:
                return False
        return True
    return False



print(bisect(2024))


# Ex 5

def f(x):
    if x < -3:
        return 2 * x + 1
    if x == - 3:
        return 0
    if x > -3:
        return 3 * x ** 2 + 6 * x - 5

print(f(3))


# Ex 6

def interval(a, b, c):
    if a <= c <=  b:
        return True
    else:
        return False

print(interval(1,5,3))



# Ex 7

def sort(a, b, c):
    maxim = max(a, b, c)
    minim = min(a, b ,c)
    mediana = a + b + c - maxim - minim

    return maxim, mediana, minim

print(sort(23,45,13))


# Ex 9
import math
def cerc(r):
    disc = 2 * math.pi * r
    arie = math.pi * r**2
    return disc, arie

print(cerc(2))

