#Write a program which accepts file name from user and open that file and display the contents of that file on screen.

def main():
    print("Enter File Name : ")
    FileName = input()
    data= open(FileName , "w")
    data.write("Hi\n")
    data.write("Marvellous InfoSystem")
    data.close()

    Result = open(FileName,"r")
    ret = Result.read()
    print(ret)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_2.py
#Enter File Name :
#input.txt
#Hi
#Marvellous InfoSystem
