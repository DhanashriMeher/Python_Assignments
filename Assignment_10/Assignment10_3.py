#Write a program which contains filter(),map( ) and reduce() in it.Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
#filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase by 10. Reduce will return product of all that numbers


CheckNumber = lambda no : (no >= 70 and no <= 90)
IncreaseFun = lambda no : no + 10
ReduceFun = lambda A,B : A * B

def FilterX(Task,Values):
    Result = []
    for i in Values:
        Ret = Task(i)
        if(Ret == True):
            Result.append(i)
    return Result

def MapX(Task,values):
    Result = []
    for i in values:
        Ret = Task(i)
        Result.append(Ret)
    return Result

def reduceX(Task,values):
    Result1 = 1
    for no in values:
        Result1 = Task(Result1,no)
    return Result1

def main():
    Data = input("Enter list : ")
    Result = [int(no) for no in Data.split()]
    print("Input Data :" ,Result)

    FData = list(FilterX(CheckNumber,Result))
    print("Filter output",FData) 

    MData = list(MapX(IncreaseFun,FData))
    print("Map Output",MData) 

    RData = reduceX(ReduceFun ,MData)
    print("Reduce output : ",RData) 

if __name__ == "__main__":
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_3.py
#Enter list :4 34 36 76 68 24 89 23 86 90 45 70
#nput Data  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#Filter output [76, 89, 86, 90, 70]
#Map Output: [86, 99, 96, 100, 80]
#Reduce Output 6538752000     




