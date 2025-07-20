#Create a bar plot of student names vs Total marks

import pandas as pd
import matplotlib.pyplot as plt

def main():

    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    print(df)

    plt.figure(figsize=(8,5))
    plt.plot(df['Name'],df['Total'],color = 'skyblue')
    plt.xlabel('Name Of Students')
    plt.ylabel('Total Marks')
    plt.title("My bar plot")
    plt.show()

if __name__ == "__main__":
    main()
