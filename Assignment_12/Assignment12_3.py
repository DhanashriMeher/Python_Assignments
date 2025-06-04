#Write a program which contains one class named as Arithmetic.
#Arithmetic class contains three instance variable as Value1,Value2.
#Inside init method initialise all instance variables to 0.
#There are three instance method inside class as Accept(),Addition(),Substraction(),Multiplication(),Division()
#Accept method will accept value of Value1 and Value2 from user.
#Addition() method will perform addition of Value1,Value2 and return result.
#Substraction() method will perform Substraction of Value1,Value2 and return result.
#Multiplication() method will perform Multiplication of Value1,Value2 and return result.
#Division() method will perform Division of Value1,Value2 and return result.
#After designing the above class call all instance methods by creating multiple objects.


class Arithmetic():

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Addition(self):
        self.Value3 = self.Value1 +self.Value2
        return self.Value3
 
    def Substraction(self):
        self.Value3 = self.Value1 - self.Value2
        return self.Value3

 
    def Multiplication(self):
        self.Value3 = self.Value1 * self.Value2
        return self.Value3

    def Division(self):
        if self.Value2 != 0:
            self.Value3= self.Value1 / self.Value2
            return self.Value3
        else:
            return "Error: Division by zero"

        #self.Value3 = self.Value1 / self.Value2
        #return self.Value3


    def Accept(self):  
        self.Value1 = float(input("Enter Value1 : "))
        self.Value2 = float(input("Enter Value2 : "))
        #print("Value2: " ,self.Value2)
        #print("Value1: ",self.Value1)

def main():
    print("\nArithmetic Operation1: ")
    obj1 =Arithmetic()
    obj1.Accept()
    print("Addition : " ,obj1.Addition())
    print("Substraction : " ,obj1.Substraction())
    print("Multiplication : " ,obj1.Multiplication())
    print("Division : " ,obj1.Division())
 
    print("\nArithmetic Operation2: ")
    obj2 =Arithmetic()
    obj2.Accept()
    print("Addition : " ,obj2.Addition())
    print("Substraction : " ,obj2.Substraction())
    print("Multiplication : " ,obj2.Multiplication())
    print("Division : " ,obj2.Division())
 
if __name__ == "__main__":
    main()

#OUTPUT
#Arithmetic Operation1:
#Enter Value1 : 5
#Enter Value2 : 6
#Addition :  11.0
#Substraction :  -1.0
#Multiplication :  30.0
#Division :  0.8333333333333334

#Arithmetic Operation2:
#Enter Value1 : 2.3
#Enter Value2 : 5.6
#Addition :  7.8999999999999995
#Substraction :  -3.3
#Multiplication :  12.879999999999999
#Division :  0.4107142857142857

 


