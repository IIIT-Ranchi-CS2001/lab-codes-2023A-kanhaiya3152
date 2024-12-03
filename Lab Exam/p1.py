import pandas as pd

data = pd.read_csv("3rd_sem\AQI_Data.csv")

df = pd.DataFrame(data)


print("Cities with highest and lowest average AQI values : ")
di=dict(df.groupby('City')['AQI'].mean().sort_values(ascending=False))

li=list(di.keys())
print("Cities with highest average AQI values is ",li[0]," with values ",di[li[0]])
print("Cities with lowest average AQI values is ",li[-1]," with values ",di[li[-1]])