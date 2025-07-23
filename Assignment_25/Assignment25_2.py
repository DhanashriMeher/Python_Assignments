#Detect column data types and convert 'Age' from float to int
#data =  {'Name' : ['A','B','C'] , 'Age' : [21.0,22.0,23.0]}

import pandas as pd

def main():
    data =  {'Name' : ['A','B','C'] , 'Age' : [21.0,22.0,23.0]}

    df = pd.DataFrame(data)
    print(df.dtypes)

    df['Age'] =df['Age'].astype(int) 

    print("\nAfter Conversion:")
    print(df.dtypes)   

    print(df)

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_2.py
#Name     object
#Age     float64
#dtype: object

#After Conversion:
#Name    object
#Age      int64
#dtype: object
#  Name  Age
#0    A   21
#1    B   22
#2    C   23    