import pandas as pd 
import sys 

df = pd.read_csv(sys.argv[1],delimiter='\t')

df['Action'] = df['Action'].replace("UpdateTextField", "UpdateTextArea", regex=True)

print(df['Problem Name'].head())

df.to_csv(sys.argv[2], sep='\t')