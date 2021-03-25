from human import Human
from cat import Cat
def walking(any_mammal):
    any_mammal.walk()

h1 = Human()

c1 = Cat()
c2 = Cat()
walking(h1)
walking(c1)
walking(c2)
