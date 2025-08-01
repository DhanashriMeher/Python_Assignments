import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def fakerealnewsdb():
    Line = "*"*100
    df1 = pd.read_csv("Fake.csv")
    df2 = pd.read_csv("True.csv")

    print(df1.head())
    print(df2.head())
    print(Line)

    #created new column label
    df1['label']= 0
    df2['label']= 1

    combined_df = pd.concat([df1,df2],ignore_index= True)
    print(combined_df.head())
    print(Line)

    #drop missing value
    combined_df= combined_df[['title','text','label']].dropna()

    combined_df['content'] =combined_df['title'] + " " +combined_df['text']
    print(combined_df['content'].head())
    print(Line)
    
    #TF-IDF vectorization
    tfidf = TfidfVectorizer(stop_words= 'english' ,max_df= 0.7)

    x = tfidf.fit_transform(combined_df['content'])
    y = combined_df['label']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2,random_state= 42)
 
    logReg1 = LogisticRegression()
    DecTree1 = DecisionTreeClassifier(max_depth=5)
     
    #using fit for models
    logReg1.fit(x_train, y_train)
    DecTree1.fit(x_train, y_train)

    logReg2 = LogisticRegression()
    DecTree2 = DecisionTreeClassifier(max_depth=5)

   #using fit for Voting
   #Soft voting
    voting_soft = VotingClassifier(
        estimators = [
            ('logReg' ,logReg2),
            ('dectree' ,DecTree2)
        ],
        voting='soft'
    )

    voting_soft.fit(x_train,y_train)

    #Hard Voting
    voting_hard = VotingClassifier(
        estimators =[
            ('logReg' ,logReg2),
            ('dectree' ,DecTree2)
        ],
        voting = 'hard'
    )
    voting_hard.fit(x_train,y_train)

    y_pred = logReg1.predict(x_test)
    y_predDectree = DecTree1.predict(x_test)

    y_predvothard = voting_hard.predict(x_test)
    y_predvotingsoft = voting_soft.predict(x_test)

    print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))
    print("Decision Tree Accuracy:", accuracy_score(y_test, y_predDectree))

    print("Hard Voting Accuracy:", accuracy_score(y_test, y_predvothard))
    print("Soft Voting Accuracy:", accuracy_score(y_test, y_predvotingsoft))
    print(Line)

    # Confusion Matrices
    print("Confusion Matrix - Logistic Regression:\n", confusion_matrix(y_test, y_pred))
    print("Confusion Matrix - Decision Tree:\n", confusion_matrix(y_test, y_predDectree))
    print("Confusion Matrix - Hard Voting:\n", confusion_matrix(y_test, y_predvothard))
    print("Confusion Matrix - Soft Voting:\n", confusion_matrix(y_test, y_predvotingsoft))
    print(Line)


def main():
    fakerealnewsdb()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment\Assignment_32>python FakeRealPredict.py
#                                               title  ...               date
#0   Donald Trump Sends Out Embarrassing New Year’...  ...  December 31, 2017
#1   Drunk Bragging Trump Staffer Started Russian ...  ...  December 31, 2017
#2   Sheriff David Clarke Becomes An Internet Joke...  ...  December 30, 2017
#3   Trump Is So Obsessed He Even Has Obama’s Name...  ...  December 29, 2017
#4   Pope Francis Just Called Out Donald Trump Dur...  ...  December 25, 2017

#[5 rows x 4 columns]
#                                               title  ...                date
#0  As U.S. budget fight looms, Republicans flip t...  ...  December 31, 2017
#1  U.S. military to accept transgender recruits o...  ...  December 29, 2017
#2  Senior U.S. Republican senator: 'Let Mr. Muell...  ...  December 31, 2017
#3  FBI Russia probe helped by Australian diplomat...  ...  December 30, 2017
#4  Trump wants Postal Service to charge 'much mor...  ...  December 29, 2017

#[5 rows x 4 columns]
#****************************************************************************************************
#                                               title  ... label
#0   Donald Trump Sends Out Embarrassing New Year’...  ...     0
#1   Drunk Bragging Trump Staffer Started Russian ...  ...     0
#2   Sheriff David Clarke Becomes An Internet Joke...  ...     0
#3   Trump Is So Obsessed He Even Has Obama’s Name...  ...     0
#4   Pope Francis Just Called Out Donald Trump Dur...  ...     0

#[5 rows x 5 columns]
#****************************************************************************************************
#0     Donald Trump Sends Out Embarrassing New Year’...
#1     Drunk Bragging Trump Staffer Started Russian ...
#2     Sheriff David Clarke Becomes An Internet Joke...
#3     Trump Is So Obsessed He Even Has Obama’s Name...
#4     Pope Francis Just Called Out Donald Trump Dur...
#Name: content, dtype: object
#****************************************************************************************************
#Logistic Regression Accuracy: 0.9858574610244989
#Decision Tree Accuracy: 0.9956570155902005
#Hard Voting Accuracy: 0.9916481069042317
#Soft Voting Accuracy: 0.9957683741648107
#****************************************************************************************************
#Confusion Matrix - Logistic Regression:
# [[4663   70]
# [  57 4190]]
#Confusion Matrix - Decision Tree:
# [[4697   36]
# [   3 4244]]
#Confusion Matrix - Hard Voting:
# [[4718   15]
# [  60 4187]]
#Confusion Matrix - Soft Voting:
# [[4698   35]
# [   3 4244]]
#****************************************************************************************************
