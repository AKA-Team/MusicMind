import pandas as pd

plays_header = ['userID','songID','plays']

print "[LOADING] train_triplets"
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)
print "[LOADING] Songs Data"
songs_df = pd.read_csv('../csv/unique_tracks.csv', sep=',', header=0)

n_entries = plays_df.count()[0]
n_tracks = songs_df.count()[0]
n_users = plays_df.userID.unique().shape[0]
n_songs = plays_df.songID.unique().shape[0]

print '\nAnalysis:'
print '- Number of unique songs  = ' + str(n_tracks)
print '- Number of plays entries  = ' + str(n_entries)
print '- Number of users = '+str(n_users)
print '- Number of songs listened to = '+str(n_songs)
