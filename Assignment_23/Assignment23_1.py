#Q1 : Create a DataFrame for student marks and print basic information like shape,columns,
#data types.

#data = {
#    'Name':['Amit','Sagar','Pooja'],
#    'Math':[85,90,78],
#    'Science':[92,88,80],
#    'English':[75,85,82]  
#   }

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)
    print(df)

    print("Dimension of DataFrame is : \n",df.shape)

    print("Columns of DataFrame : \n",df.columns)

    print("Datatype is: \n",df.dtypes)

if __name__ == "__main__":
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_1.py
#   Name  Math  Science  English
#0   Amit    85       92       75
#1  Sagar    90       88       85
#2  Pooja    78       80       82
#Dimension of DataFrame is :
# (3, 4)
#Columns of DataFrame :
# Index(['Name', 'Math', 'Science', 'English'], dtype='object')
#Datatype is:
# Name       object
#Math        int64
#Science     int64
#English     int64
#dtype: object