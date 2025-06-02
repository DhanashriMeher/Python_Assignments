#Write a program which contains filter(),map( ) and reduce() in it.Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
#filter should filter out all such numbers which are even.Map Function will calculate its square.
# Reduce will return addition of that numbers.


EvenNo = lambda n : (n % 2 == 0)
SqrNo = lambda n : n * n
AdditionNo = lambda A,B : A + B

def filterX(Task ,values):
    Result = []
    for no in values:
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)

    return Result

def MapX(Task,Values):
    Result = []
    for i in Values:
        Ret = Task(i)
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
    print("Input List : " ,number_list)

    FData = list(filterX(EvenNo,number_list))
    print("list after Filter: ",FData)

    MData = list(MapX(SqrNo,FData))
    print("List after Map: ",MData)

    RData = reduceX(AdditionNo,MData)
    print("Output of Reduce: ",RData)

if __name__ == "__main__":
     main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_4.py
#Enter numbers : 5 2 3 4 3 4 1 2 8 10
#Input List :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#list after Filter:  [2, 4, 4, 2, 8, 10]
#List after Map:  [4, 16, 16, 4, 64, 100]
#Output of Reduce:  204


