#Write a recursive function to calculate sum from 1 to n.

sum = 0
def SumRec(no):
    global sum
    if(no >= 1):
        sum = sum + no
        SumRec(no-1)
    return sum 

def main():
    print(SumRec(5))

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_6.py
#15    

