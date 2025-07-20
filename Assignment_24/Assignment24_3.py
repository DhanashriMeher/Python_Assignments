#Group students by Gender and calculate average marks.

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

    Average_Marks = df.groupby('Gender')[['Math','Science','English']].mean()

    print(Average_Marks)


if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_24>python Assignment24_3.py
#        Math  Science  English
#Gender
#Female  84.0     84.0     83.5
#Male    85.0     92.0     75.0    