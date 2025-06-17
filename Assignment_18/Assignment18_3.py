#Write a program which accepts file name from user and create new file named as Demo.txtnand copy all contents from existing 
#file into new line. Accept file name through command line argument.

import sys 
import os

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide the source file name as a command-line argument.")
        return

    source_file = sys.argv[1]

    if not os.path.exists(source_file):
        print("File is not present in the directory")

    try:
        First_file = open(source_file,"r")
        Second_file = open("Output.txt","w")

        for line in First_file:
            Second_file.write(line)

    except Exception as e:
        print("An error occurred:", e)
      
if __name__ == "__main__":
    main()    
