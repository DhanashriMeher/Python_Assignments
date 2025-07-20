#Normalize the 'Math' scores using Min-Max scaling.

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

#Normalized Value= (max−min) / (x−min)

    df['Normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    
    print(df)

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_24>python Assignment24_1.py
#    Name  Math  Science  English  Normalized
#0   Amit    85       92       75    0.583333
#1  Sagar    90       88       85    1.000000
#2  Pooja    78       80       82    0.000000
        
