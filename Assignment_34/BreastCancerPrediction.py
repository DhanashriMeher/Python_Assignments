import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix,classification_report,precision_score,recall_score
from sklearn.datasets import load_breast_cancer

def BreastCancerPredict():
    data = load_breast_cancer()
    #print(data)
    df = pd.DataFrame(data.data,columns=data.feature_names)

    for column in df.columns:
        print(df[column].head())

    #Missing Values
    print(df.isnull().sum())

    #statistics
    print(df.describe())  

    df['target'] = data.target

    #Split Dataset
    x = df.drop('target',axis= 1)
    y = df['target']

    #Normalise /scale features
    scaleData = StandardScaler()
    scaler = scaleData.fit_transform(x)

    #split into train/test
    x_train,x_test,y_train,y_test = train_test_split(scaler,y,test_size= 0.2,random_state= 42)

    #Build model
    model = LogisticRegression()
    model.fit(x_train,y_train)

    #Evaluate
    y_pred = model.predict(x_test)

    #Accuracy
    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy: " ,accuracy*100)

    #Visualization of Feature correlation
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(),cmap = 'coolwarm',annot = False)
    plt.title("Correlation Heatmap")
    plt.show()

    #Confusion matrix
    con_matrix = confusion_matrix(y_test,y_pred)

    plt.figure(figsize=(6,8))
    sns.heatmap(con_matrix,annot = True,cmap = "plasma" ,linecolor = "black",fmt="d")
    plt.title("Confusion Matrix")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    #F1-score ,precision,recall
    f1score = f1_score(y_test,y_pred)
    print("F1-Score : ",f1score)

    prec = precision_score(y_test,y_pred)
    print("Precision Score : ",prec)

    rec = recall_score(y_test,y_pred)
    print("Recall Score : " ,rec)

    #Classification matrix
    class_Matrix = classification_report(y_test,y_pred)
    print("Classifiaction Report : \n" ,class_Matrix)

def main():
    BreastCancerPredict()

if __name__ =="__main__":
    main()

'''
Conclusion : 
            1.Logistic regression model achieved high accuracy.
            2.The model is well-suited for predicting whether a tumor is malignant or benign.
            3.Precision , recall and F1 Score are all close to 1.0 
'''