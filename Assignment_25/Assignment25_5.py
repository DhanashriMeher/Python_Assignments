#Create a Dataframe with 'Age' and 'Purchased' columns and split into train/test sets
#data = {'Age' : [22,25,47,52,46,56],'Purchased': [0,1,1,0,1,0]}

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age' : [22,25,47,52,46,56],'Purchased': [0,1,1,0,1,0]}

    df = pd.DataFrame(data)
     
    x = df[['Age']]
    y = df['Purchased']
    x_train,y_train,x_test,y_test = train_test_split(x,y,test_size =0.2 ,random_state= 42)

    print("x_train : \n" ,x_train)
    print("y_train: \n",y_train)
    print("x_test : \n",x_test)
    print("y_test : \n",y_test)

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_5.py
#x_train :
#    Age
#5   56
#2   47
#4   46
#3   52
#y_train:
#    Age
#0   22
#1   25
#x_test :
#5    0
#2    1
#4    1
#3    0
#Name: Purchased, dtype: int64
#y_test :
#0    0
#1    1
#Name: Purchased, dtype: int64
