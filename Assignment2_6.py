#write a program which accept one number and display below pattern
#input : 5
#Output : 
#* * * * *
#* * * *
#* * *
#* *
#*

def main():
    num = int(input("Enter number :"))
    for i in range(num):  
        for j in range(i,num):
            print(" * " ,end= " ")
        print()        

if __name__ == "__main__":
    main()

#output
# C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_6.py
#Enter number :5
 #*   *   *   *   *
 #*   *   *   *
 #*   *   *
 #*   *
 #*    