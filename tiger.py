class Tiger:
    def __init__(self,name,health_level = 8 ,happiness_level = 5, age = "unknown"):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level
    
    def display_info(self):
        print(
            f"Name: {self.name}",
            f"Type: {type(self).__name__}",
            f"Age: {self.age}",
            f"Heath: {self.health}",
            f"Happiness: {self.happiness}",
            sep="\n" , end="\n\n")
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self