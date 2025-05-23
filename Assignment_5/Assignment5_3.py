#Voting eligibilty checker
#Accept age from the user and check whether the person is eligible to vote.(Age should be 18 or above).

def CheckAge(no):
    if(no >= 18):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")

def main():
    Result = int(input("Enter age: "))
    CheckAge(Result)            

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_3.py
#Enter age: 19
#Eligible to vote.

#C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_3.py
#Enter age: 10
#Not Eligible to vote.    

   
