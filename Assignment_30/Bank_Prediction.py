import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,roc_curve,auc
from sklearn.ensemble import VotingClassifier


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
    log_clf = LogisticRegression()
    dt_clf = RandomForestClassifier(n_estimators= 150, max_depth=7,random_state= 42)
    knn_clf = KNeighborsClassifier(n_neighbors= 3)

    voting_clf = VotingClassifier(
        estimators= [
            ('lr',log_clf),
            ('dt',dt_clf),
            ('knn',knn_clf)   
        ],
        voting = 'soft'
    )   
    voting_clf.fit(x_train,y_train)

    y_pred = voting_clf.predict(x_test)

    y_prob = voting_clf.predict_proba(x_test)[:, 1]

    print(f"Information about logistic registration")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

    confusionMatrix = confusion_matrix(y_test,y_pred)
    print("Confusion Matrix :",confusionMatrix)
    print(Line)

    ROCCurve = roc_auc_score(y_test,y_pred)
    print("ROC Curve : ",ROCCurve)

    #PLOT Confusion matrix
    plt.figure(figsize=(6,4))
    sns.heatmap(confusionMatrix,annot= True,fmt = 'd')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    fpr, tpr, thresholds = roc_curve(y_test, y_prob)

    # Compute the Area Under the Curve (AUC)
    roc_auc = auc(fpr, tpr)

    # Plot the ROC curve
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, color='blue', label=f'ROC Curve')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')  # Diagonal line
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()


def main():
    BankPredict("bank-full.csv")

if __name__ =="__main__":
    main()
