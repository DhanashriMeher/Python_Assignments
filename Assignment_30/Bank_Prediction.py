import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score

def BankPredict(Datapath):

    Line = '*' * 100
    df = pd.read_csv(Datapath , sep=';')
    print(df.head())
    print(Line)

    print("Missing values : \n" ,df.isnull().sum())
    print(Line)

    data = df.drop(columns='poutcome')
    print(data)
    print(Line)

    print("Statistics of distribution : \n",df.describe())
    print(Line)

    sns.countplot(x = 'y',data =df)
    plt.title("Class Distribution")
    plt.show()


    for col in df.select_dtypes(include = 'object'):
       df[col] =df[col].replace('unknown',df[col].mode()[0])
       df[col] = LabelEncoder().fit_transform(df[col])

    print(df.head())    
    print(Line)

    x=df.drop(columns = ['y'])
    y =df['y']

    scale = StandardScaler()
    scaler = scale.fit_transform(x)
    print(scaler)
    print(Line)

    x_train,x_test,y_train,y_test = train_test_split(scaler,y,test_size=0.2,random_state=42)
    
    #Checking model with KNN
    logisticmodel = LogisticRegression(max_iter=1000)
    knn_model = KNeighborsClassifier(n_neighbors=5)
    rf_model = RandomForestClassifier(random_state=42)

    # Train models
    logisticmodel.fit(x_train, y_train)
    knn_model.fit(x_train, y_train)
    rf_model.fit(x_train, y_train)

    ylogpred = logisticmodel.predict(x_test)
    #yknnpred = knn_model.predict(x_test)
    #rfpred = rf_model.predict(x_test)

    y_prob = ylogpred.predict_proba(x_test)[:, 1]

    print(f"Information about logistic registration")
    print("Accuracy:", accuracy_score(y_test, ylogpred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, ylogpred))
    print("Classification Report:\n", classification_report(y_test, ylogpred))
    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

    confusionMatrix = confusion_matrix(y_test,ylogpred)
    print("Confusion Matrix :",confusionMatrix)
    print(Line)

    ROCCurve = roc_auc_score(y_test,ylogpred)
    print("ROC Curve : ",ROCCurve)

    #PLOT Confusion matrix
    plt.figure(figsize=(6,4))
    sns.heatmap(confusionMatrix,annot= True,fmt = 'd')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    



def main():
    BankPredict("bank-full.csv")

if __name__ =="__main__":
    main()