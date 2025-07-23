#Apply One-Hot Encoding to a 'Department' column
#data = {'Department' :['HR','IT','Finance','HR','IT']}

import pandas as pd

def main():
    data = {'Department' :['HR','IT','Finance','HR','IT']}
    df = pd.DataFrame(data)

    model = pd.get_dummies(df,columns=['Department']).astype(int)
    print(model)

if __name__ == "__main__":
    main() 

 #OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_4.py
#   Department_Finance  Department_HR  Department_IT
#0                   0              1              0
#1                   0              0              1
#2                   1              0              0
#3                   0              1              0
#4                   0              0              1   
