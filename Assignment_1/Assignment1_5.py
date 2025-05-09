#Write a program which display 10 to 1 on screen
#Output : 10 9 8 7 6 5 4 3 2 1

def main():
    for i in range(10,0,-1):
        print(i ,end = " ")
    
if __name__ == "__main__":
    main()    

# C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_5.py
#10 9 8 7 6 5 4 3 2 1

#OR

def main():
    print(list(range(10,0,-1)))
    
if __name__ == "__main__":
    main()    

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_5.py
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]   


