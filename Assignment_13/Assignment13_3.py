#Write a program which contains one class names as Numbers
#Arithematic class contains one instance variable as Value
#Inside init method initialise that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(),ChkPerfect(),SumFactors(),Factors()
#ChkPrime() method will returns true if number is prime otherwise return false
#ChkPerfect() method will returns true if number is perfect otherwise return false
#Factors() method will return addition of all factors.Use this method in any another method as a helper method if required.
#After designing the above class call all instance methods by creating multiple objects.

class Numbers:

    def __init__(self,Value):
        self.Value = Value    
  
    def chkPrime(self):
        if self.Value < 2:
            return False
        else:
            for i in range(2,self.Value):
                if(self.Value % i == 0):
                    return False
            return True    

    def Factors(self):
        Fact =[]
        for i in range(1,self.Value):
            if (self.Value % i == 0):
                Fact.append(i)
        return Fact    

    def SumFactors(self):
        return sum(self.Factors())    
    
    def ChkPerfect(self):
        return self.SumFactors() == self.Value


def main():
    Ret = int(input("Enter Value :"))
    obj1 = Numbers(Ret)
    print("Prime Number :",obj1.chkPrime())
    print("The number is perfect or not : ",obj1.ChkPerfect())
    print("Factors of number : ",obj1.Factors())
    print("SumFactors : ",obj1.SumFactors())

    Ret1 = int(input("\nEnter Value :"))
    obj2 = Numbers(Ret1)
    print("Prime Number :",obj2.chkPrime())
    print("The number is perfect or not : ",obj2.ChkPerfect())
    print("Factors of number : ",obj2.Factors())
    print("SumFactors : ",obj2.SumFactors())

if __name__ == "__main__":
    main()    

#OUTPUT
# Enter Value :8
#Prime Number : False
#The number is perfect or not :  False
#Factors of number :  [1, 2, 4]
#SumFactors :  7

#Enter Value :6
#Prime Number : False
#The number is perfect or not :  True
#Factors of number :  [1, 2, 3]
#SumFactors :  6
    