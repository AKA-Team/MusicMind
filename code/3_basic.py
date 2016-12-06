import pandas as pd

"""
A basic recommendation system can be simply to recommend the most listened songs.
"""

# Loading the DB
print "[LOADING] train_triplets..."
plays_header = ['userID','songID','plays']
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

print "[LOADING] Song Data"
songs_df = pd.read_csv('../csv/song_data.csv', sep=',', header=0)

# Get the most listened songs
songs_total_listens = plays_df.groupby('songID')['plays'].sum().sort_values(ascending=False).to_frame()
print "\n# Top songs with most total listens:"
print songs_total_listens.head().to_string()


# Join songs with data
songs_total_listens = songs_total_listens.join(songs_df.set_index('songID')).sort_values('plays', ascending = False)
print "\n# Top Songs with most total lisens:"
print songs_total_listens.head().to_string().encode('utf-8')
