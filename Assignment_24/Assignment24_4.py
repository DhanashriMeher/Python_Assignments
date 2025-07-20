#Plot a pie chart of subject marks for 'Sagar'.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    sagar_Chart = df[df['Name'] == 'Sagar']

    marks = sagar_Chart[['Math', 'Science', 'English']].values.flatten()
    subjects = ['Math', 'Science', 'English']
 
    plt.figure(figsize = (6,6))
    plt.pie(marks,labels =subjects,autopct = '%1.1f%%')
    plt.title("Sagar's subject marks")
    plt.show()

if __name__ == "__main__":
    main()