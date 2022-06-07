from lion import Lion
from tiger import Tiger
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self

    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            return self


zoo1 = Zoo("John's Zoo").add_tiger("Shere Khan").add_lion("Nala").add_lion("Simba").add_tiger("Rajah").print_all_info().display_info()

