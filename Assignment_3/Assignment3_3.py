#Write a program which accept N numbers from user and store it into list.Return Minimum number from that list
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#output: 5

def MinimumNo():
    numbers = []
    N = int(input("Enter number : "))
    for i in range(N):
        num = int(input("Enter elements : "))
        numbers.append(num)
    Minno = min(numbers)
    print("List : ",numbers)
    print("Maximum number is : " ,Minno)

def main():
   MinimumNo()

if __name__ =="__main__":
 main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_3>Python Assignment3_3.py
#Enter number : 4
#Enter elements : 13
#Enter elements : 5
#Enter elements : 45
#Enter elements : 7
#List :  [13, 5, 45, 7]
#Maximum number is :  5