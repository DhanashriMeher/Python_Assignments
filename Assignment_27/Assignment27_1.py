import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn import metrics


def Advertisement(Datapath):
    Line = '*' *50
    df = pd.read_csv(Datapath)

    print(df.head())
 
    print(Line)
    df.drop(columns = ['Unnamed: 0'],inplace= True)
    print(df)
    print(Line)

    print("Missing value \n :" ,df.isnull().sum())

    print(Line)

    x = df[['TV','radio','newspaper']]
    y =df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.5,random_state= 42)

    model = LinearRegression()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)
    print("Prediction\n : ",y_pred)

    print(Line)
    result = pd.DataFrame({'Actual Dataset' :y_test ,'Predicted Dataset ' : y_pred})
    print(result)
    print(Line)

    MSE = metrics.mean_squared_error(y_test,y_pred)
    print("Mean Squared Error ",MSE)

    RMSE = np.sqrt(MSE)
    print("Root Mean Squared Error ",RMSE)

    r2_score = metrics.r2_score(y_test,y_pred)
    print("R2 Score : ",r2_score)

def main():
    Advertisement("Advertising.csv")    

if __name__ == "__main__":
    main()    