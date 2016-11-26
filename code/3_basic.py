import pandas as pd

# Loading the DB
print "[LOADING] train_triplets..."
plays_header = ['userID','songID','plays']
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

print "[LOADING] unique_tracks"
tracks_header = ['trackID','songID','artist','title']
tracks_df = pd.read_csv('../csv/unique_tracks.csv', sep='\t', names=tracks_header)

# Get the most listened songs
songs_total_listens = plays_df.groupby('songID')['plays'].sum().sort_values(ascending=False).to_frame()
print "\n# Top songs with most total listens:"
print songs_total_listens.head().to_string()


# Join songs with tracks
tracks_total_listens = songs_total_listens.join(tracks_df.set_index('songID')).sort_values('plays', ascending = False)
print "\n# Top tracks with most total lisens:"
print tracks_total_listens.head().to_string().encode('utf-8')
