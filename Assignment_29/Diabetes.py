import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix,precision_score,recall_score
import matplotlib.pyplot as plt

def DiabetesPredictor(Datapath):
    Line = '*'*50
    df = pd.read_csv(Datapath)
    print(df.head)
    print(Line)

    #Column info
    print(df.dtypes)
    print(df.info())
    print(Line)

    #Check for null values
    print("Missing Values : \n",df.sum().isnull())
    print(Line)

    #Display statistics
    print(df.describe())
    print(Line)

    #Plot distribution
    sns.countplot(x='Outcome' , data = df)
    plt.title("Distribution of target variable")
    plt.show()

    #Histogram of Bloodpressure vs Outcome
    sns.histplot(df['Outcome'],bins = 10,kde= True)
    plt.title("Histogram to Show Outliers in 'Outcome'")
    plt.xlabel("Outcome")
    plt.ylabel("BloodPressure")
    plt.show()

    #Boxplot
    sns.boxplot(y=df['Outcome'])
    plt.title("Boxplot to Detect Outliers in Outcome")
    plt.ylabel("Outcome")
    plt.show()

    #check missing values of Glucose and Blood pressure.
    df.isnull().sum()

    df.fillna(df.mean(numeric_only= True),inplace = True)
    print(df)
    print(Line)

    x=df.drop(columns = ['Outcome'])
    y =df['Outcome']

    scaler = StandardScaler()
    data = scaler.fit_transform(x)

    print(data)
    print(Line)

    x_train,x_test,y_train,y_test = train_test_split(data,y,test_size=0.2,random_state=42)

    #Checking model with KNN
    model = KNeighborsClassifier()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
   
    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy score :" ,accuracy)
    print(Line)

    confMatrix = confusion_matrix(y_test,y_pred)
    print("Confusion Matrix :",confMatrix)
    print(Line)

    F1Score = f1_score(y_test,y_pred)
    print("F1-Score : " ,F1Score)
    print(Line)

    prec_score  =precision_score(y_test,y_pred)
    print("Precision Score : ",prec_score)
    print(Line)

    rec  = recall_score(y_test,y_pred)
    print("Recall Score : ",rec)
    print(Line)

    plt.figure(figsize=(6,4))
    sns.heatmap(confMatrix,annot= True,fmt = 'd')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    #Checking model with Decision Tree
    decisionModel = tree.DecisionTreeClassifier(criterion= 'entropy',max_depth= 5,random_state= 42)
    decisionModel.fit(x_train,y_train)

    y_pred = decisionModel.predict(x_test)

    print("Decision Tree Evaluation Metrics")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Precision Score:\n", precision_score(y_test, y_pred))
    print("Recall Score:\n", recall_score(y_test, y_pred))
    print("F1 Score:\n", f1_score(y_test, y_pred))

    print(Line)

    final_predictions = decisionModel.predict(x_test)

    final_pred = pd.DataFrame(x_test,columns = x.columns)
    final_pred['Predicted_Outcome'] = final_predictions
    final_pred['Actual_Outcome'] = y_test.values
                                    
    print(final_pred.head())
    print(Line)

    final_pred.to_csv("diabetes_predictions.csv", index=False)
    print("Predictions saved to 'diabetes_predictions.csv'")


def main():
    DiabetesPredictor("diabetes.csv")

if __name__ == "__main__":
    main()        