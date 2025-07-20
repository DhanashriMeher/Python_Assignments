#Display students who scored more than 85 in science

import pandas as pd

def main():
    data = {
   'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
     }

    df = pd.DataFrame(data)

    result = df[df['Science'] > 85]

    print(result)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_4.py
#   Name  Math  Science  English
#0   Amit    85       92       75
#1  Sagar    90       88       85