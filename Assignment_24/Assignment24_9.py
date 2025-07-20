#Rename math to mathematics.

import pandas as pd

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    df = df.rename(columns={'Math': 'Mathematics'})

    print(df)

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_24>python Assignment24_9.py
#    Name  Mathematics  Science  English
#0   Amit           85       92       75
#1  Sagar           90       88       85
#2  Pooja           78       80       82

