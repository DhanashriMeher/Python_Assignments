import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_curve,auc,roc_auc_score


def BreastCancerPrediction():
    Line = '*' * 100
    data = load_breast_cancer()

    x = pd.DataFrame(data.data,columns = data.feature_names)
    y = pd.Series(data.target,name ='target')

    print("Features :" ,x.head())
    print("Target Variable : ",y.head())

    print("Missing values : \n" ,x.isnull().sum())
    print("Missing values of target variable : \n" ,y.isnull().sum())
    print(Line)
 
    scale = StandardScaler()
    scaler =scale.fit_transform(x)
    print(scaler)
    print(Line)

    x_train,x_test,y_train,y_test = train_test_split(scaler,y,test_size= 0.2,random_state= 42)

    Dt_clf = DecisionTreeClassifier(max_depth=5)
    rf_clf = RandomForestClassifier(n_estimators= 150, max_depth=7,random_state= 42)

    voting_clf = VotingClassifier(
        estimators=[
            ('dt',Dt_clf),
            ('rf_clf',rf_clf)
        ],
        voting = 'soft'
    )

    voting_clf.fit(x_train,y_train)

    rf_model = voting_clf.named_estimators_['rf_clf']
    print("Random Forest Feature Importances:")
    print(rf_model.feature_importances_)


    y_pred = voting_clf.predict(x_test)

    y_prob = voting_clf.predict_proba(x_test)[:, 1]

    print("Accuracy" ,accuracy_score(y_test,y_pred) * 100)

    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

    confusionMatrix = confusion_matrix(y_test,y_pred)
    print("Confusion Matrix :",confusionMatrix)
    print(Line)

    plt.figure(figsize=(6,4))
    sns.heatmap(confusionMatrix,annot= True,fmt = 'd')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    ROCCurve = roc_auc_score(y_test,y_prob)
    print("ROC Curve : ",ROCCurve)

    fpr, tpr, thresholds = roc_curve(y_test, y_prob)

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

    #Feature Importance
    fitted_dt = voting_clf.named_estimators_['dt']
    importance = fitted_dt.feature_importances_
    feature_names = data.feature_names

    feat_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
    }).sort_values(by='Importance', ascending=False)

    print(feat_importance_df)

def main():
    BreastCancerPrediction()

if __name__ =="__main__":
    main()

