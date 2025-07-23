#Split a Dataframe with multiple features into train_test for supervised learning

#data = {
#   'Age' :[25,30,45,35,22],
#    'Salary' :[50000,60000,80000,65000,45000],
#    'Purchased' :[1,0,1,0,1]
#}

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    data = {
        'Age':[25,30,45,35,22],
        'Salary' :[50000,60000,80000,65000,45000],
        'Purchased':[1,0,1,0,1]
        }

    df =pd.DataFrame(data)

    X = df[['Age','Salary']]
    y = df['Purchased']

    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

    print("X_train:\n", x_train)
    print("\nX_test:\n", x_test)
    print("\ny_train:\n", y_train)
    print("\ny_test:\n", y_test)


    model = LogisticRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)
    print("Predicted : ",y_pred)

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_10.py
#X_train:
#    Age  Salary
#4   22   45000
#2   45   80000
#0   25   50000
#3   35   65000

#X_test:
#    Age  Salary
#1   30   60000

#y_train:
#4    1
#2    1
#0    1
#3    0
#Name: Purchased, dtype: int64

#y_test:
#1    0
#Name: Purchased, dtype: int64
#Predicted :  [1]






