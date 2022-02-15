class PartyAnimal:  # declare class
    x = 0  # data

    def party(self):  # method
        self.x = self.x+1
        print("So far", self.x)


an = PartyAnimal()  # object
# method run
# an.x = 32
an.party()
an.party()
an.party()
