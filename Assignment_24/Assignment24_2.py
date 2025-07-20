#Create a Gender column and perform one hot encoding.

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Female','Female']

    One_hotEncoding = pd.get_dummies(df,columns = ['Gender'])
    One_hotEncoding[['Gender_Female','Gender_Male']] = One_hotEncoding[['Gender_Female','Gender_Male']].astype(int)

    print(One_hotEncoding)

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_24>python Assignment24_2.py
#    Name  Math  Science  English  Gender_Female  Gender_Male
#0   Amit    85       92       75              0            1
#1  Sagar    90       88       85              1            0
#2  Pooja    78       80       82              1            0
    