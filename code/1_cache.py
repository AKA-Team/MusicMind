import pandas as pd

plays_header = ['userID','songID','plays']
songs2tracks_header = ['songID', 'trackID']
tracks_header = ['trackID','songID','artist','title']

print "[LOADING] train_triplets"
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)
print "[LOADING] songs_to_tracks.csv"
songs2tracks_df = pd.read_csv('../csv/song_to_tracks', sep='\t', names=songs2tracks_header)
print "[LOADING] unique_tracks"
tracks_df = pd.read_csv('../csv/unique_tracks.csv', sep='\t', names=tracks_header)

n_entries = plays_df.count()[0]
n_tracks = tracks_df.count()[0]
n_users = plays_df.userID.unique().shape[0]
n_songs = plays_df.songID.unique().shape[0]

print '\nAnalysis:'
print '- Number of unique tracks  = ' + str(n_tracks)
print '- Number of plays entries  = ' + str(n_entries)
print '- Number of users = '+str(n_users)
print '- Number of songs = '+str(n_songs)
