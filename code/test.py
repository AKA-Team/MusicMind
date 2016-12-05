import pandas as pd

plays_header = ['userID','songID','plays']

print "[LOADING] train_triplets"

df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

df.columns = ['UserID','songID','plays']

print df

pivot = df.pivot(index='UserID', columns='songID', values='plays')

print pivot



