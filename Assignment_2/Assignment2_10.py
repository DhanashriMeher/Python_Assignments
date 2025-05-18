#write a program which accept number from user and return addition of digits in that number
#Input :5187934  Output :37

def SumOfDigit(number):
  sum_digits = 0
  for digit in str(number):
     sum_digits = sum_digits + int(digit)
  return sum_digits

def main():
    num = int(input("Enter a number: "))
    result = SumOfDigit(num)
    print("Sum of digits:", result)
  
if __name__ == "__main__":
  main()

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_10.py
#Enter a number: 123
#Sum of digits: 6

#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_10.py
#Enter a number: 5187934
#Sum of digits: 37 