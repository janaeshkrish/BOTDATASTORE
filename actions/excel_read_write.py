import pandas as pd
import os

def DataStore(name,gender,city,occupation):

    if os.path.isfile('user_data.xlsx'):
        df = pd.read_excel('user_data.xlsx')

        df.append([[name,gender,city,occupation]])

        df.to_excel('user_data.xlsx',index=False)

    else:
        #File doesnot exsist
        df = pd.DataFrame([[name,gender,city,occupation]],columns=['name','gender','city','occupation'])

        df.to_excel('user_data.xlsx',index=False)



def Fetchdata(column,occupation):

    if os.path.isfile('user_data.xlsx'):
        df = pd.read_excel('user_data.xlsx')

        data = df[column][df["occupation"]==occupation]
        return data.to_list()

    else:
        #File doesnot exsist
        return ["There is no data."]