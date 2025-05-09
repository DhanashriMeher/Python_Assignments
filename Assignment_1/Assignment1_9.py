#Write a program which display first 10 even numbers on screen.
#output 2 4 6 8 10 12 14 16 18 20

def EvenNo():
    print(list(range(2,21,2)))

if __name__ == "__main__":
    EvenNo()    

 #OUTPUT
 #C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_9.py
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
 
 #OR    

def EvenNo():
    for i in range(1, 11):
        print(2*i, end=" ")

if __name__ == "__main__":
    EvenNo()    


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_9.py
#2 4 6 8 10 12 14 16 18 20