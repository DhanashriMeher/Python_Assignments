#Create a class Calculator with methods for add,substract,multiply,divide.Ask user input for values and call methods.

class Calculator():

    def __init__(self):
        self.Number1 = int(input("Enter number1 :"))
        self.Number2 = int(input("Enter number2 :"))        

    def Add(self):
        return self.Number1 + self.Number2
        
    def Substract(self):
        if (self.Number1 > self.Number2) :
            return self.Number1 - self.Number2
        else:
            print("For Substraction Number1 is smaller than number2")

    def Multiply(self):
        return self.Number1 * self.Number2

    def Divide(self):
        if (self.Number1 > self.Number2) :
            return self.Number1 / self.Number2
        else:
            print("For Division number1 is smaller than number2")
        
def main():
    obj = Calculator()

    print("\nAddition is : ",obj.Add())
    print("Substraction is : ",obj.Substract())
    print("Multiplication is : " ,obj.Multiply())
    print("Division is : ",obj.Divide())

if __name__ == "__main__":
    main()        

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_6.py
#Enter number1 : 10
#Enter number2 :5

#Addition is :  15
#Substraction is :  5
#Multiplication is :  50
#Division is :  2.0
        