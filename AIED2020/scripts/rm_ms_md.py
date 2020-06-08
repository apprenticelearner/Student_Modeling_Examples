import pandas as pd 
import sys 

df = pd.read_csv(sys.argv[1],delimiter='\t')

df['Problem Name'] = df['Problem Name'].replace("MS.", "M ", regex=True)
df['Problem Name'] = df['Problem Name'].replace("MD.", "M ", regex=True)

print(df['Problem Name'].head())

df.to_csv(sys.argv[2], sep='\t')