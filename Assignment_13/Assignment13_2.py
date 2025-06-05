#Write a Program which contains one class named as BankAccount.
#BankAccount class contains two instance variable as Name and Amount.
#that class contains one class variable as ROI which is initialise to 10.5
#Inside init method initialise all name and amount variables by accepting the values from user.
#There are four instance methods inside class as Display(),Deposit(),Withdraw(),CalculateInterest().
#Deposit() method will accept the amount from user and add that value in class instance variable Amount.
#Withdraw() method will accept amount to be withdrawn from user and substract that amount from class instance variable amount
#CalculateInterest() method calculate the interest based on Amount by considering rate of interest which is class variable as ROI
#& Display method will display value of all the instance variables as Name and Amount.After Designing the above class call all instance methods
#by creating multiple objects.

class BankAccount():

    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter account holder name: ")
        self.Amount = float(input("\nEnter initial amount: "))
   
    def Display(self):
        print("\nAccount Holder Name: ", self.Name)
        print("Current Balance is: ",self.Amount)


    def Deposit(self):
        self.DepositAmt = float(input("Enter Deposit Amount: "))
        self.Amount = self.Amount + self.DepositAmt
        print("Total Amount : ",self.Amount)

    def Withdraw(self):
        self.WithdrawAmount = float(input("\nEnter Withdraw Amount : "))
        if self.WithdrawAmount <= self.Amount:
            print("Remaining Amount : ",self.Amount - self.WithdrawAmount)
        else:
            print("Insufficient balance.")
    

    def CalculateInterest(self):
        print("Interest is : ",(self.Amount * BankAccount.ROI)/100)

def main():
    print("\n -----Account1-----")
    obj1 = BankAccount()
    obj1.Deposit()
    obj1.Display()
    obj1.Withdraw()
    obj1.CalculateInterest()
   # obj1.Display()
    
if __name__ == "__main__" :
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_13>python Assignment13_2.py

 #-----Account1-----
#Enter account holder name: Dhanashri

#Enter initial amount: 15000
#Enter Deposit Amount: 5000
#Total Amount :  20000.0

#Account Holder Name:  Dhanashri
#Current Balance is:  20000.0

#Enter Withdraw Amount : 8000
#Remaining Amount :  12000.0
#Interest is :  2100.0



        



