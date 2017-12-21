#1. Write a sample Python code to assign values to an instance using dot notation?
class Dog:
    dogCount = 1
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Dog.dogCount += 1


    def displayDogCount(self):
        print "Dog Count %d" % Dog.dogCount

    def displayDog(self):
        print "Name: ", self.name, ", Color: ", self.color






# "This would create first object of Dog class"
dog1 = Dog("Zara", "Blue")
# "This would create second object of Dog class"
dog2 = Dog("Manni", "Black")

dog1.displayDog()
dog2.displayDog()
print "Total Dog %d" % Dog.dogCount



#2. Write a sample Python code to define a function?

def myFunction():
    print "This is a defined function, or check code above"