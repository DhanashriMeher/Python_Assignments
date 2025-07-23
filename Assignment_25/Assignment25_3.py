#Apply label Encoding to a 'City' column
#data = {'City' : ['Pune','Mumbai','Delhi','Pune','Delhi']}

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {'City' :['Pune','Mumbai','Delhi','Pune','Delhi']}
    df = pd.DataFrame(data)

    model = LabelEncoder()
    
    df['Encoding'] = model.fit_transform(df['City'])

    print(df)

if __name__ == "__main__":
    main()    
    
#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_3.py
#     City  Encoding
#0    Pune         2
#1  Mumbai         1
#2   Delhi         0
#3    Pune         2
#4   Delhi         0    
