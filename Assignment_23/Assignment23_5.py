#Replace 'Pooja' with 'Puja' in the 'Name' column.

import pandas as pd
def main():
    data = {
   'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
     }

    df = pd.DataFrame(data)
    df['Name'] =df['Name'].replace('Pooja','Puja')
    print(df['Name'])

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_5.py
#0     Amit
#1    Sagar
#2     Puja
#Name: Name, dtype: object    

