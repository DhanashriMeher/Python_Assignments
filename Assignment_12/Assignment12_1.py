#Write a program which contains one class named as Demo
#Demo class contains two instance variable as no1,no2
#That class contains one class variable as Value
#There are two instance methods of class as Fun and Gun which displays values of instance variable
#Initialise instance variable in init method by accepting the values from user.
#After creating the class create the two objects of Demo class as
#obj1 = Demo(11,21)
#obj2 = Demo(51,101)

#Now call the instance methods as 
#obj1.Fun()
#obj2.Fun()
#obj1.Gun()
#obj2.Gun()

class Demo:

    Value = "OOP Concepts"

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Inside Fun method : ")
        print("Value of no1" ,self.no1)
        print("Value of no2" ,self.no2)

    def Gun(self):        
        print("Inside Gun Method : ")
        print("Value of no1" ,self.no1)
        print("Value of no2" ,self.no2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

    print("Class variable Value =", Demo.Value)

if __name__ == "__main__":
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_12>python Assignment12_1.py
#Inside Fun method :
#Value of no1 11
#Value of no2 21
#Inside Fun method :
#Value of no1 51
#Value of no2 101
#Inside Gun Method :
#Value of no1 11
#Value of no2 21
#Inside Gun Method :
#Value of no1 51
#Value of no2 101
#Class variable Value = OOP Concepts
