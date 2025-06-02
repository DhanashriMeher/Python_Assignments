#Write a recursive function to Count how many zeros are in the given number.

def Count_Zeros(no):
    if no == 0:
        return 1
    
    last_digit = no % 10 
    Remain_number = no // 10  

    if last_digit == 0:
        count = 1
    else:
        count = 0

    return count + Count_Zeros(Remain_number)

def main():
    no1 = int(input("number : "))
    print(Count_Zeros(no1))

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_5.py
#number : 1020300
#5