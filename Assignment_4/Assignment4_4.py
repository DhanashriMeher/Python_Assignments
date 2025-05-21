#Write a program which contains filter(),map( ) and reduce() in it.Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
#filter should filter out all such numbers which are even.Map Function will calculate its square.
# Reduce will return addition of that numbers.

ChechEvenNo = lambda No:(No % 2 == 0)
SquareNo = lambda No : No ** 2
Add = lambda A,B : A+B

def filterX(Task ,values):
    Result = []
    for no in values:
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)

    return Result

def mapX(Task,values):
    Result = []
    for no in values:
        Ret = Task(no)
        Result.append(Ret)

    return Result    

def reduceX(Task,values):
    Result = 0 
    for no in values:
        Result = Task(Result , no)
    return Result

def main():

    Data = input("Enter numbers : ")
    number_list = [int(num) for num in Data.split()]
    print("Input data : " ,number_list)

    FData = list(filterX(ChechEvenNo ,number_list))
    print("Filter Data : ",FData)

    MData = list(map(SquareNo,FData))
    print("Map Data : ",MData)

    RData = reduceX(Add,MData)
    print("Reduce Data : ",RData)

if __name__ == "__main__":
     main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_4.py
#Enter numbers : 5 2 3 4 3 4 1 2 8 10
#Input data :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#Filter Data :  [2, 4, 4, 2, 8, 10]
#Map Data :  [4, 16, 16, 4, 64, 100]
#Reduce Data :  204