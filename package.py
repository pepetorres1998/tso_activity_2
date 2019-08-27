class Package:
    def __init__(self, max_weight):
        self.elements = []
        self.weight = 0
        self.value = 0
        self.max_weight = max_weight

    def add_element(self, element):
        if(element.weight + self.weight <= self.max_weight):
            self.elements.append(element)
            self.value += element.value
            self.weight += element.weight
