#write a program which accept one number and display below pattern
#input : 5
#Output : 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def main():
    number = int(input("Input : "))
    for i in range(number) :  
        for j in range(number):
            print("*" ,end = " ")
        print()

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_2.py
#Input : 5
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *    