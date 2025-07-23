#Replace values in 'Marks' less than 50 with 'Fail' using where()
#data ={'Marks' :[45,67,88,32,76]}

import pandas as pd

def PassFail(Marks):
    if Marks < 50:
        return "Fail"
    else :
        return "Pass"
    
def main():
    data ={'Marks' :[45,67,88,32,76]}
    df = pd.DataFrame(data)
 
    df['Marks'] = df['Marks'].where(df['Marks']> 50 ,'Fail')

    print(df)

if __name__ == "__main__":
    main()     


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_9.py
#  Marks
#0  Fail
#1    67
#2    88
#3  Fail
#4    76
