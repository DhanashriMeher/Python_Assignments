#Plot a line chart of marks for 'Amit' across all subject.

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

    DataOfAmit = df[df['Name'] == 'Amit']
    Marks = [DataOfAmit['Math'].values[0],DataOfAmit['Science'].values[0],DataOfAmit['English'].values[0]]

    subjects = ['Maths','Science','English']

    plt.plot(subjects,Marks)
    plt.title("Amit's Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

if __name__ == "__main__" :
    main()


