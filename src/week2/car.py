####################################################################
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
####################################################################



class Tesla:

    def __init__(self,colour,model,hp):
        self.colour = colour
        self.model = model
        self.hp = hp

    def cust_colour(self):
        orig_colour = self.colour
        if orig_colour == 'red':
            orig_colour = 'Orange'
            print(orig_colour)
        elif orig_colour == 'Black':
            orig_colour = 'Gray'
            print(orig_colour)
        else:
            orig_colour = self.colour
            print(orig_colour)

    def car_hp(self):
        self.hp = self.hp
        print(self.hp)


ramesh = Tesla('Black','X',1000)
ramesh.cust_colour()
ramesh.car_hp()
