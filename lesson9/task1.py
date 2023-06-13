class auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        self.age += 1
a = auto("Lada", 6, "purple", "Sedan", 1100)
print(a.age)
print(a.mark)