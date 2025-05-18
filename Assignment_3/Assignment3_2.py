#Write a program which accept N numbers from user and store it into list.Return Maximum number from that list
#Input : Number of elements : 7
#Input Elements :13 5 45 7 4 56 34
#output: 56

def MaximumNo():
    numbers = []
    N = int(input("Enter number : "))
    for i in range(N):
        num = int(input("Enter elements : "))
        numbers.append(num)
    Maxno = max(numbers)
    print("List : ",numbers)
    print("Maximum number is : " ,Maxno)

def main():
   MaximumNo()

if __name__ =="__main__":
 main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_3>Python Assignment3_2.py
#Enter number : 7
#Enter elements : 13
#Enter elements : 5
#Enter elements : 45
#Enter elements : 7
#Enter elements : 4
#Enter elements : 56
#Enter elements : 34
#List :  [13, 5, 45, 7, 4, 56, 34]
#Maximum number is :  56
