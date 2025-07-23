#Replace Multiple values in a column using a dictionary.
#data = {'Grade':['A+','B','A','C','B+']}

#Replace as 
#'A+':'Excellent'
#'B':'Very Good'
#'A':'Good'
#'C':'Average'
#'B+':'Poor'

import pandas as pd

def main():
    data = {'Grade':['A+','B','A','C','B+']}

    df = pd.DataFrame(data)
    replace_dictionary = {'A+':'Excellent','B':'Very Good','A':'Good','C':'Average','B+':'Poor'}
   
    df['Grade'] = df['Grade'].replace(replace_dictionary)
    
    print(df)

if __name__ == "__main__":
    main()    


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_25>python Assignment25_6.py
#       Grade
#0  Excellent
#1  Very Good
#2       Good
#3    Average
#4       Poor




