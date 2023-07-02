#Christian Allen
#July 2, 2023
#The purpose of this code is to implement the flower class and show it's attributes and methods

class Flower: 
    def __init__(self, name): 
        self.name = name #Initializing the class name "Flower"

    def grow(self):
        print("The " +self.name + " is growing.") #Used to print a message that the flower is "growing"

    def bloom(self):
        print("The " + self.name + " is blooming.") #Used to print a message that the flower is "blooming"

def main():
    flower1 = Flower("Rose") #Creating a Flower object from the Flower class and calling it a "Rose"
    flower1.grow() #Calls the "grow" method for the Rose
    flower1.bloom() #Calls the "bloom" method for the Rose
    flower2 = Flower("Daisy") #Creates a Flower object from the Flower class called "Daisy"
    flower2.grow() #Calls the "grow" method for the Daisy
    flower2.bloom() #Calls the "bloom" method for the Daisy
    flower3 = Flower("Lotus") #Creates a Flower object from the Flower class called "Lotus"
    flower3.grow() #Calls the "grow" method for the Lotus
    flower3.bloom() #Calls the "bloom" method for the Lotus

if __name__ == "__main__":
  main() 