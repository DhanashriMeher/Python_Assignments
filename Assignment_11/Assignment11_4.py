#Power function using recursion
#Write a recursive function to calculate x^n

def PowRec(no1,no2):
    if no2 == 0:
        return 1
    elif(no2 > 0):
        ret = no1 * PowRec(no1,no2-1)  
        return ret
        
def main():
    print(PowRec(2,3))

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_4.py
#8
