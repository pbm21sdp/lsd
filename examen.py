
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
        lista = srd(tree["left"]) + [tree["value"]] + srd(tree["right"])
        return lista
    else:
        return []

def crescator(lista, lista1=[]):
    lista1 = lista.sort()
    print(lista1)
    if (lista1 == lista):
        print("Arborele este binar de cautare")
    else:
        print("Arborele nu este binar de cautare")


print(crescator(srd(binary_tree)))
print(crescator(srd(arbore)))
