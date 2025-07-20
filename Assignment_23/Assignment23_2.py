#Use the dataframe from Q1. and print descriptive statistics using .describe()

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    print("Descriptive Statistics \n" ,df.describe())

if __name__ == "__main__":
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_2.py
#Descriptive Statistics
#            Math    Science    English
#count   3.000000   3.000000   3.000000
#mean   84.333333  86.666667  80.666667
#std     6.027714   6.110101   5.131601
#min    78.000000  80.000000  75.000000
#25%    81.500000  84.000000  78.500000
#50%    85.000000  88.000000  82.000000
#75%    87.500000  90.000000  83.500000
#max    90.000000  92.000000  85.000000