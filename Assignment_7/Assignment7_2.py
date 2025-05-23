#Accept a list of integers from the user and use the map() function to double each value.

DoubleNo = lambda x : x * x

def MapX(Task,Values):
    Result = []
    for i in Values:
        Ret = Task(i)
        Result.append(Ret)

    return Result

def main():

    Data = input("Enter list : ")
    number_list = [int(num) for num in Data.split()]
    print("list : " ,number_list)

    MData = list(MapX(DoubleNo,number_list))
    print("Doubled list: ",MData)

if __name__ == "__main__":
    main()    

#output
#C:\Users\Dhanashri\Desktop\Python\Assignment_7>python Assignment7_2.py
#Enter list : 1 2 3 4 5
#list :  [1, 2, 3, 4, 5]
#Doubled list:  [1, 4, 9, 16, 25]    
    