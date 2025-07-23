import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

def WinePredictor(Datapath):

    Line = '*'*50
    df = pd.read_csv(Datapath)
    print(df.head)
    print(Line)

    print("Missing Value : \n",df.isnull().sum())
    print(Line)
  
    x = df.drop(columns = ['Class'])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler .fit_transform(x)

    print(x_scale)
     
    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size = 0.2 ,random_state = 42)

    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors= k)
        model.fit(x_train,y_train)
        y_pred =model.predict(x_test)
        accuracy= accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)
        
    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]    
    print("Best value of k is : ",best_k)

    model = KNeighborsClassifier(n_neighbors= k)
    model.fit(x_train,y_train)
    y_pred =model.predict(x_test)
    accuracy= accuracy_score(y_test,y_pred)

    print("Final best accuracy is : ",accuracy*100)
    sm = confusion_matrix(y_test,y_pred)
    print(sm)

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()        