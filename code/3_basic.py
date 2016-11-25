import pandas as pd

print "[LOADING] train_triplets..."
plays_header = ['userID','songID','plays']
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

# Calculate the most listened songs
songs_total_listens = plays_df.groupby('songID')['plays'].sum().sort_values(ascending=False).to_frame()
print "Top songs with most total listens: "
print songs_total_listens.head()
