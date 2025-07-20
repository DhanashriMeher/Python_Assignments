#Drop the 'English' column from original dataframe.

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    data1 = df.drop('English',axis=1)
    print(data1)

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_10.py
#    Name  Math  Science
#0   Amit    85       92
#1  Sagar    90       88
#2  Pooja    78       80