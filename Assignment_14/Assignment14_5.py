#Create a class BankAccount with account_number,name and balance.Use __init__ and create methods for deposit,withdraw,
#and displaying balance.

class BankAccount():

    def __init__(self,acnt_number,name,Balance):
        self.acnt_number = acnt_number
        self.name = name
        self.Balance = Balance

    def Deposit(self,depositAmt):
        print("\nEnter deposit amount:" ,depositAmt)
        self.Balance = self.Balance + depositAmt
        return self.Balance

    def Withdraw(self,WithdrawAmt):
        print("\nEnter Amount to be Withdraw :" ,WithdrawAmt)
        return self.Balance - WithdrawAmt
    
    def DispBalAnce(self):
        print("Account Number : ",self.acnt_number)
        print("Name of AccountHolder : ",self.name)
        print("Balance : " ,self.Balance)
        
def main():
    obj = BankAccount(1002012,"Mr.Akshay",50000)
    obj.DispBalAnce()

    print("Balance After Deposit : ",obj.Deposit(20000))
    print("Balance After Withdraw : " ,obj.Withdraw(30000))

if __name__ == "__main__":
    main()        

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_5.py
#Account Number :  1002012
#Name of AccountHolder :  Mr.Akshay
#Balance :  50000

#Enter deposit amount: 20000
#Balance After Deposit :  70000

#Enter Amount to be Withdraw : 30000
#Balance After Withdraw :  40000
            

  
     

        