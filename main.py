from element import Element

if(__name__=='__main__'):
    with open('values.txt', 'r') as f:
        values = [Element(line.rstrip()) for line in f.readlines()]
        print([value.id for value in values])

