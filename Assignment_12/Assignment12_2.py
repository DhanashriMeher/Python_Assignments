#Write a program which contains one class named as Circle.
#Circle class contains three instance variables as Radius,Area,Circumference.
#That class contains three instance variable as PI which is initialise to 3.14
#Inside Init method initialise all instance variable to 0.0
#There are three instance methods inside a class as Accept(),CalculateArea(),CalculateCircumference(),Display()
#Accept method will accept value of Radius from user.
#CalculateArea() method will calculate area of circle and store it into instance variable Area.
#CalculateCircumference() method will calculate circumference of circle and store it into instance variable circumference.
#And Display() method will display value of all the instance variables like radius,Area,Circumference.
#After designing the above class call all instance methods by creating multiple objects.

class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI *self.Radius

    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: " ,self.Area)
        print("Circumference: ",self.Circumference)

def main():
    print("Circle1 :")
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print("\nCircle2 :")
    obj2 = Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

    print("\nCircle3 :")
    obj3 = Circle()
    obj3.Accept()
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_12>python Assignment12_2.py
#Circle1 :
#Enter radius : 4
#Radius: 4.0
#Area: 50.24
#Circumference: 25.12

#Circle2 :
#Enter radius : 2.3
#Radius: 2.3
#Area: 16.610599999999998
#Circumference: 14.443999999999999

#Circle3 :
#Enter radius : 8
#Radius: 8.0
#Area: 200.96
#Circumference: 50.24
