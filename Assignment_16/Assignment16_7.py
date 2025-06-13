#Create a file marks.txt with Student name and marks. Then read the file and display student who scored more 
#than 75 marks.

def main():
    File = open("marks.txt", "w")
    File.write("Sachin 82\n")
    File.write("Vinod 67\n")
    File.write("Snehal 91\n")
    File.write("Lata 73\n")

    print("Students who scored more than 75 marks:")
    File = open("marks.txt", "r")
    for line in File:
        name, marks = line.strip().split()
        if int(marks) > 75:
            print(f"{name}: {marks}")
       
if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_7.py
#Students who scored more than 75 marks:
#Sachin: 82
#Snehal: 91