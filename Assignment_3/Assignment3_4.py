#Write a program which accept N numbers from user and store it into list.Accept one another number from user 
# and return frequency of that number from list

#Input :Number of elements : 11
#Input Elements:13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#output : 3


def main():
    n = int(input("Number of elements: "))

    elements = []
    print("Enter the elements:")
    for _ in range(n):
        num = int(input())
        elements.append(num)

    search_element = int(input("Element to search: "))

    frequency = elements.count(search_element)

    print("Output:", frequency)

if __name__ == "__main__":
    main()

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_3>Python Assignment3_4.py
#Number of elements: 11
#Enter the elements:
#13
#5
#45
#7
#4
#56
#5
#34
#2
#5
#65
#Element to search: 5
#Output: 3   