class rajiv_gandhi:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def nativePlace(self):
        print('Delhi')

    def role(self):
        print('Ex Prime Minister')

    def parents(self):
        print('Foriz & Indhira')

class human:

    def __init__(self,gender):
        self.sex = gender
        print(self.sex)

    def male(self):
        self.height = 6
        self.weight = 60
        print(f'My height is {self.height} and my weight is {self.weight}')

    def female(self):
        self.height = 5.6
        self.weight = 55
        print(f'My height is {self.height} and my weight is {self.weight}')
