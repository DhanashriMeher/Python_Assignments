#Accept a list of numbers and use the filter() function to keep only even numbers.

EvenNo = lambda x : (x% 2 == 0)

def FilterX(Task,Values):
    Result =[]
    for i in Values:
        Ret = Task(i)
        if(Ret == True):
           Result.append(i)

    return Result

def main():

    Data = input("Enter list : ")
    number_list = [int(num) for num in Data.split()]
    print("list : " ,number_list)

    FData = list(FilterX(EvenNo ,number_list))
    int_list = [int(x) for x in FData]

    print("Even numbers : " ,int_list)


if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_7>python Assignment7_3.py
#Enter list : 1 2 3 4 5 6
#list :  [1, 2, 3, 4, 5, 6]
#Even numbers :  [2, 4, 6]    