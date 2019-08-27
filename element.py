import pdb
import json

class Element:
    def __init__(self, values):
        id, value, weight = values.split(',')
        self.id = int(id)
        self.value = float(value)
        self.weight = float(weight)
        self.relation = self.value / self.weight

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

if(__name__=='__main__'):
    element = Element("1,2,3")
    pdb.run('element')
