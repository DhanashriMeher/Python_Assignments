#Print Triangle pattern using Nested Loops
#*
#* *
#* * *
#* * * *

def pattern():
    num = 4
    for i in range(0,num):
        for j in range(0,i+1):
            print("*",end = " ")
        print()    

def main():
    pattern()

if __name__ == "__main__":
    main()            

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_6.py
#*
#* *
#* * *
#* * * *