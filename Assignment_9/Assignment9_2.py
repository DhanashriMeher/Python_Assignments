#Write a python program using multiprocessing.Process to square a list of numbers using multiple processes.

import multiprocessing

def SquareOfTwo(no1):
    new_list = [x ** 2 for x in no1]
    print("Square of list : ",new_list)
     
def main():
    Data = input("number for square list : ")
    sqrList = [int(no) for no in Data.split()]
    print("List : ",sqrList)

    P1 = multiprocessing.Process(target= SquareOfTwo ,args = (sqrList,))
 
    P1.start()

    P1.join()

if __name__ == "__main__"   :
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_9>python Assignment9_2.py
#number for square list : 1 2 3 4 5 6
#List :  [1, 2, 3, 4, 5, 6]
#Square of list :  [1, 4, 9, 16, 25, 36]
    