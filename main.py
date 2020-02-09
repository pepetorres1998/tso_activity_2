from element import Element
from package import Package
import pdb

if(__name__=='__main__'):
    with open('values.txt', 'r') as f:
        values = [Element(line.rstrip()) for line in f.readlines()]
        p = Package(30)
        values.sort(key=lambda x: x.value, reverse=True)

        for value in values:
            p.add_element(value)

        print('Elementos en la mochila:', '\n')
        print(p.elements, '\n')
        print('Valor total de la mochila: {total}'.format(total=p.value))
        print('Peso total de la mochila: {weight}'.format(weight=p.weight))
