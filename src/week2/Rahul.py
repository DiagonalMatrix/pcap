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

    def who_am_I(self):
        self.name = self.fname
        self.sirname = self.lname
        print(f"my father's name is {self.name} {self.sirname}!!")

class Rahul(rajiv_gandhi):
    pass

############################################################################
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
############################################################################

whoAmI = Rahul('Rajiv','gandhi')
whoAmI.nativePlace()
whoAmI.role()
whoAmI.parents()
whoAmI.who_am_I()
