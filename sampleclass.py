# classes & objects (chapter 14)
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()

x = list()
print(type(x))
print(dir(x))

y = 'Hello there'
print(dir(y))

an = PartyAnimal()
print(type(an))

class PartyAnimal2:
    x = 0
    def __init__ (self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
    def __del__ (self):
        print('I am destructed', self.x)


an = PartyAnimal2()
an.party()
an.party()
an = 42
print('an contains', an)

class PartyAnimal3:
    x = 0
    name = ""
    def __init__ (self, z):
        self.name = z
        print(self.name, 'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)
    def __del__ (self):
        print('I am destructed', self.x)

a = PartyAnimal3('Alice')
a.party()

b = PartyAnimal3("Bob")
b.party()

class FootballFan (PartyAnimal3):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

a = PartyAnimal3('Alice')
a.party()

b = FootballFan('Bob')
b.party()
b.touchdown()

