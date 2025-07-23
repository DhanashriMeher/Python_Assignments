#Normalize 'Age' column using Min-Max Scaling.
#data = {'Age': [18,22,25,30,35]}

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {'Age' : [18,22,25,30,35]}

    df =pd.DataFrame(data)

    model = MinMaxScaler()

    Min_Max_Scaler = model.fit_transform(df)

    ScalerData = pd.DataFrame(Min_Max_Scaler,columns=df.columns)

    print(ScalerData)

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_7.py
#        Age
#0  0.000000
#1  0.235294
#2  0.411765
#3  0.705882
#4  1.000000    