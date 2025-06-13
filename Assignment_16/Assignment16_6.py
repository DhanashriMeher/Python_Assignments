#Write a python program to copy the contents of one file (source file) into another file(destination file)

def main():
    print("Enter Source file name : ")
    FileName = input()
    ret = open(FileName,"r")
    
    print("Enter Destination file : ")
    FileName1 = input()
    ret1 = open(FileName1,"a")
    
    for line in ret:
        ret1.write(line)

if __name__ == "__main__":
    main()

        

