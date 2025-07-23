import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def PlayPredictor(Datapath):
    Line = "*" *50
    df = pd.read_csv(Datapath)

    print("First few records of the dataset are :")
    print(Line)
    print(df.head())
    print(Line)

    df = df.drop(columns=['Unnamed: 0'])
    print(df)
    print(Line)

    modelwhether = LabelEncoder()
    modelTemp = LabelEncoder()
    modelPlay = LabelEncoder()

    df['Whether'] = modelwhether.fit_transform(df['Whether'])
    df['Temperature'] = modelTemp.fit_transform(df['Temperature'])
    df['Play'] =modelPlay.fit_transform(df['Play'])
    print(df)

    print(Line)

    X = df [['Whether','Temperature']]
    y = df['Play']

    x_train,x_test,y_train,y_test = train_test_split(X,y,random_state = 42)

    modelKNN = KNeighborsClassifier(n_neighbors=3)
    modelKNN.fit(x_train,y_train)

    y_pred = modelKNN.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy of KNN : ",accuracy)

    print(Line)

    WhetherValue = input("Enter whether : ").strip().capitalize()
    TempValue = input("Enter Temperature : ").strip().capitalize()

    Wether = modelwhether.transform([WhetherValue])[0]
    Temp = modelTemp.transform([TempValue])[0]

    input_df = pd.DataFrame([[Wether, Temp]], columns=['Whether', 'Temperature'])
    result = modelKNN.predict(input_df)
    data = modelPlay.inverse_transform(result)
    print("Final Prediction : ",data[0])

def main():
  PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
  main()  




  