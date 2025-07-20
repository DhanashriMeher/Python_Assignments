#Count how many student pass

import pandas as pd

def PassFail(total):
    if total >= 250: 
        return 'pass'  
    else:
        return 'Fail'
    
def main():
    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]  
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math'] + df['Science'] + df['English']    
   
    df['Status'] = df['Total'].apply(PassFail)
    print(df)
   
    count =(df['Status'] == 'pass').sum()
    print("Total number of students are pass : ", count)

if __name__ == "__main__":
    main()   

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_24>python Assignment24_6.py
#    Name  Math  Science  English  Total Status
#0   Amit    85       92       75    252   pass
#1  Sagar    90       88       85    263   pass
#2  Pooja    78       80       82    240   Fail
#Total number of students are pass :  2