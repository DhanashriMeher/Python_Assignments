#Create a class Vehicle with method start().Derive class Car and Override the method start() with additional behavior.Show
#method overriding

class Vehicle:

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):

    def start(self):
        print("Car is Running")
        print("Switching ON lights and AC")

def main():
    obj1 = Vehicle()
    obj1.start()

    obj =Car()
    obj.start()        
    
if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_8.py
#Vehicle is starting
#Car is Running
#Switching ON lights and AC
