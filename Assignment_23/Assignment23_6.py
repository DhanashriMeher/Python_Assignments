#Sort the dataframe by 'Total' marks in descending order.

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)
    
    df['Total'] = df[['Math', 'Science' ,'English']].sum(axis = 1)
    df.sort_values(by = 'Total',ascending = False ,inplace = True)
    print(df) 

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_6.py
#   Name  Math  Science  English  Total
#1  Sagar    90       88       85    263
#0   Amit    85       92       75    252
#2  Pooja    78       80       82    240