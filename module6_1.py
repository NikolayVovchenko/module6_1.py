
class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} сьел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{self.name} не может есть и погиб {food}')

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    edible = True
    def __init__(self, name):
        self.name = name



class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print('********************************')
print(a1.name)
print(p1.name)
print('--------------------------------')
print(a1.alive)
print(a2.fed)
print('--------------------------------')
a1.eat(p1)
a2.eat(p2)
print('--------------------------------')
print(a1.alive)
print(a2.fed)
print('*********************************')




