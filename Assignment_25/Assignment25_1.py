#Detect outliers in the 'salary' column using the IQR method
#data = {'Salary' : [25000,27000,29000,31000,50000,100000]}

import pandas as pd

def main():

    data = {'Salary' : [25000,27000,29000,31000,50000,100000]}

    df = pd.DataFrame(data)

    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    IQR = Q3-Q1

    lower_bound = Q1- 1.5*IQR
    Upper_bound = Q3 + 1.5*IQR

    Outliers = df[(df['Salary'] < lower_bound ) | (df['Salary'] > Upper_bound)]

    print("Outliers in Salary column : ")
    print(Outliers)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_1.py
#Outliers in Salary column :
#   Salary
#5  100000
