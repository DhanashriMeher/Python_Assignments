#Create a DataFrame with missing values and fill them with column mean

#data2 = {
#    'Name':['Amit','Sagar','Pooja']
#    'Math':[np.nan,76,88]
#    'Science':[91,no.nan,85]
#    }

import pandas as pd
import numpy as np

def main():

    data = {
     'Name':['Amit','Sagar','Pooja'],
     'Math':[np.nan,76,88],
     'Science':[91,np.nan,85]
     }
    
    df = pd.DataFrame(data)

    data1= df.fillna(df.mean(numeric_only= True))
    print(data1)
    
if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_23>python Assignment23_9.py
#    Name  Math  Science
#0   Amit  82.0     91.0
#1  Sagar  76.0     88.0
#2  Pooja  88.0     85.0
