import pandas as pd

df = pd.read_csv("VeriDosyaları/F12022Results.csv")
df.head()
df.info()
df.shape
df.isnull().values.any()
df.isnull().sum()
df["Driver"].value_counts()
pd.set_option("display.max_column",None)
df["Points"].mean()
df["Starting Grid"].mean()
df["No"].mean()
df.groupby("Driver").agg({"Points":"mean"})
df.groupby("Team").agg({"Points":["mean","sum","count"]})
df.groupby(["Driver","Team"]).agg({"Points":"mean",
                                   "Laps":"mean"})
df.describe().T
