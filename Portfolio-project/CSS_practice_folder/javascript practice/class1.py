####### Creating classes in python using self and init method ##########
class Car:
    def __init_ (self,brand,color,speed):
        self.color=color
        self.brand=brand
        self.speed=speed
    def display(self):
        print(f"brand={self.brand} , color={self.color}, speed={self.speed}")

car1=Car("Lambo","Red","120km/hr")
car2=Car("Ferrari","Yellow","100km/hr")
car3=Car("Rolls Royce","Scarlet","100km/hr")

car1.display()
car2.display()
car3.display()
