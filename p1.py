
binary_tree = {"value": 2, "left":
    {
        "value": 7, "left": None, "right":
        {
            "value": 6, "left":
            {
                "value": 5, "left": None, "right": None
            }, "right":
            {
                "value": 11, "left": None, "right": None
            },
        },
    }, "right":
                   {
                       "value": 4, "left": None, "right": None
                   }
               }

arbore = {'value': 10, 'left': {'value': 3, 'left': None, 'right': {'value': 7, 'left':
    {'value': 4, 'left': None, 'right': None}, 'right': {'value': 9, 'left': None, 'right': None}}},
          'right': {'value': 12, 'left': None, 'right': None}}


def srd(tree):
    if (tree != None):
        return srd(tree["left"]) + [tree["value"]] + srd(tree["right"])
    else:
        return []

lista1 = srd(arbore)
lista2 = lista1.copy()
lista2.sort()

def crescator(lista1, lista2):
    if(lista1 == lista2):
        print("Arborele este binar de cautare")
    else:
        print("Arborele nu este binar de cautare")

print(crescator(lista1, lista2))

