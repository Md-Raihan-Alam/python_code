class PartyAnimal:
    x = 0

    def __init__(self):  # construction
        print("I am constructed")

    def party(self):
        self.x = self.x+1
        print("So far", self.x)

    def __del__(self):  # destructions
        print("I am destructed", self.x)


an = PartyAnimal()
an.party()
an.party()
an = 45
print("an contains", an)
