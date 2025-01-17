class people:
    def __init__(self, name=None, height=156, speed=23):
        self.name = name
        self.height = height
        self.speed = speed

    def __str__(self):
        return f'I am a people and my name is {self.name}, and height {self.height}, my speed i {self.speed}'

people = people(name="Roma")
print(people.__str__())


class dog:
    def __init__(self, name="luna", weight=7, color="black", speed=36):
        self.name = name
        self.weight = weight
        self.color = color
        self.speed = speed

dog = dog(weight=7, name="Luna", color="black", speed=36)
print(f"dog weight is {dog.weight}, and name {dog.name}, color is {dog.color}, and move speed {dog.speed}")






