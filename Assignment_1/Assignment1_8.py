#Write a program which accept number from user and print that number of "*" on screen
#Input : 5   Output * * * * *

star = " * "
def pattern():
  number = int(input("Enter the value : "))
  print(number * star)
      
if __name__ == "__main__":
   pattern()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_8.py
#Enter the value : 5
# *  *  *  *  *

#OR

def pattern():
    number = int(input("Enter the value : "))
    for i in range(number):
         print("*" , end = " ")
    
if __name__ == "__main__":
   pattern()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_8.py
#Enter the value : 5
#* * * * *
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_8.py
#Enter the value : 10
#* * * * * * * * * *