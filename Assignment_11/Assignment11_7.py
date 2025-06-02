#Print Pattern using recursion
#*
#* *
#* * *
#* * * *

#normal function
#def StarPattern(n):
#    for i in range(n+1):
#        for j in range(i):
#            print("*",end = " ")
#        print()

def stars(no):
    if no == 0:
        return
    print("*" ,end = " ")
    stars(no-1)

def print_rows(n,i = 1):
    if i > n:
        return
    stars(i)
    print()
    print_rows(n,i+1)


def main():
    print(print_rows(4))

if __name__ == "__main__":
    main()    

#C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_7.py
#*
#* *
#* * *
#* * * *