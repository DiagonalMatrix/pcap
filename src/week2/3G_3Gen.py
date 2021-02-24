class grandFather():
    def __init__(self, name):
        self.name = name
        print('Hello GrandPa')

    def gp_property(self):
        return 100

class father(grandFather):
    def __init__(self,name):
        grandFather.__init__(self,name)

    def father_property(self):
        return 100

class child(father):
    def __init__(self, name):
        super().__init__(name)
        print('Hello child')

    def myNetWorth(self):
        print('Your networth')


ch1 = child('Ramesh')
ch1.gp_property()
ch1.father_property()
ch1.myNetWorth()
