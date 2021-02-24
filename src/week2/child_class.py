#######################################################################################################################
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#
#######################################################################################################################

from src.week2.parent_class import rajiv_gandhi, human

class female(human):
    def __init__(self):
        print('Brand new init')

#fm = female('Priyanks')
#fm = female()
#fm.male()
#fm.female()

#######################################################################################################################
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
#
#######################################################################################################################

class male(human):
    def __init__(self,gender,age):
        human.__init__(self,gender)
        self.gender = gender
        self.age = age
        print('Child inheritance')

    def age(self):
        self.age = self.age

#ml = male('male',25)
#ml.female()
#ml.age()

#######################################################################################################################
# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.
# If SUPER used self must not be used
#######################################################################################################################

class male1(human):
    def __init__(self,gender):
        super().__init__(gender)
        print('SUPER')

m1 = male1('male')
m1.female()

