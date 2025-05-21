#Write a program which contains filter(),map( ) and reduce() in it.Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
#filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase by 10. Reduce will return product of all that numbers

CheckNo = lambda No :(No >= 70 and No <= 90)
Increase= lambda No:No+10
Product = lambda A,B :A * B

def filterX(Task,values):
    Result = []
    for no in values:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)

    return Result    

def mapX(Task,values):
    Result = []
    for no in values:
        Ret=Task(no)
        Result.append(Ret)

    return Result        

def reduceX(Task,values):
    Result1 = 1
    for no in values:
        Result1 = Task(Result1,no)
    return Result1

def main():

    Data = input("Enter list :")
    numbers_list = [int(num) for num in Data.split()]
    print("Input Data " ,numbers_list)

    FData = list(filterX(CheckNo,numbers_list))
    print("Filter output" , FData)

    MData = list(mapX(Increase,FData))
    print(" Map Output:",MData)

    RData = reduceX(Product,MData)
    print("Reduce Output" ,RData)

if __name__ == "__main__":
     main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_3.py
#Enter list :4 34 36 76 68 24 89 23 86 90 45 70
#nput Data  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#Filter output [76, 89, 86, 90, 70]
#Map Output: [86, 99, 96, 100, 80]
#Reduce Output 6538752000     