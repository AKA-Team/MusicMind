import graphlab as gl

# Load datasets
listens = gl.SFrame.read_csv('../csv/train_triplets.csv', delimiter='\t', header=False)
listens.rename({'X1':'userID', 'X2':'songID', 'X3':'plays'})
songs = gl.SFrame.read_csv('../csv/song_data.csv')

# Build model
training_data, validation_data = gl.recommender.util.random_split_by_user(listens, 'userID', 'songID')
model = gl.recommender.create(training_data, 'userID', 'songID', target='plays')

# Recommend songs to users
recommendations = model.recommend()

# Save & show the results
recommendations.save('../recommendations')
print recommendations
