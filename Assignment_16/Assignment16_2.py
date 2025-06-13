#Write a program to read and display the contents of a file data.txt

def main():
    FileName = "data.txt"

    result = open(FileName ,"w")
    result.write("File input output programs")
    result.writelines("\nHello\nI am learning Python ,automations and Machine Learning")
    result.close()

    ret = open(FileName,"r")
    data = ret.read() 
    print(data)

    ret.close()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_2.py
#File input output programs
#Hello
#I am learning Python ,automations and Machine Learning



