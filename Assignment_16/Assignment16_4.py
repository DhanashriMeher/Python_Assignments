#Accept 10 numbers from the user and write them into a file named numbers.txt,each on a new line

def main():
    print("Enter File name: ")
    FileName = input()

    ret = open(FileName,"w")
    
    print("Enter 10 numbers : ")
    
    for i in range(10):
        Numbers = input()

        ret.write(str(Numbers)+"\n")
        print(end = "")

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_4.py
#Enter File name:
#number.txt
#Enter 10 numbers :
#7
#4
#1
#8
#5
#2
#9
#6
#3
#1
