#Write two lambda functions
#One to calculate square of a number.
#Another to calculate cube of a number.

def SquareNo(Num):
    SquareNo =lambda Num :Num * Num
    Result = SquareNo(Num)
    return Result

def CubeNo(Num):
    CubeNo = lambda Num : Num * Num * Num
    Result = CubeNo(Num)
    return Result
def main():
    number = int(input("Enter number : "))
    print("Square : ",SquareNo(number))
    print("Cube : ",CubeNo(number))

if __name__ == "__main__":
    main()    

 #OUTPUT
 #C:\Users\Dhanashri\Desktop\Python\Assignment_7>python Assignment7_1.py
#Enter number : 3
#Square :  9
#Cube :  27    