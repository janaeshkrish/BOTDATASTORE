import pandas as pd

df=pd.read_excel("user_data.xlsx")
data=df["email"][df["occupation"]=="developer"]

print(data.to_list())