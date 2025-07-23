#Fill missing values in numeric column  using interpolation 
#data ={'Marks':[80,np.nan,90,np.nan,95]}

import pandas as pd
import numpy as np

def main():
    data ={'Marks':[80,np.nan,90,np.nan,95]}

    df= pd.DataFrame(data)
    
    df['Marks'] = df['Marks'].interpolate()
    print(df)

if __name__ == "__main__":
    main()    


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_8.py
#   Marks
#0   80.0
#1   85.0
#2   90.0
#3   92.5
#4   95.0
