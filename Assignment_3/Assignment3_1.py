#Write a program which accept N numbers from user and store it into list.Return addition of all elements from that list.
#Input : Number of elements :6
#Input Elements: 13 5 45 7 4 56
#Output: 130

def Addition_Of_number():
    numbers = []
    N = int(input("Enter number : "))
    for i in range(N):
        num = int(input("Enter elements : "))
        numbers.append(num)
    total = sum(numbers)
    print("List : ",numbers)
    print("Addition of numbers : " ,total)

def main():
  Addition_Of_number()

if __name__ =="__main__":
 main()

 #OUTPUT
 #C:\Users\Dhanashri\Desktop\Python\Assignment_3>python Assignment3_1.py
#Enter number : 6
#Enter elements : 13
#Enter elements : 5
#Enter elements : 45
#Enter elements : 7
#Enter elements : 4
#Enter elements : 56
#List :  [13, 5, 45, 7, 4, 56]
#Addition of numbers :  130
    
