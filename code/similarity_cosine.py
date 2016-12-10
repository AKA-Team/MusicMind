import graphlab as gl
import sqlite3
from graphlab import SFrame as sf

# Load dataset
print "[LOADING] data"
conn = sqlite3.connect('../sqlite/msd.sqlite3')
data= gl.SFrame.from_sql(conn, "SELECT * FROM train where plays >2")

# Create Training set and test set
train_data, test_data = gl.recommender.util.random_split_by_user(data, 'userID', 'songID')

# Create the model
model = gl.recommender.create(train_data, 'userID', 'songID')

# Recommend to users
recom = model.recommend()

# Show results
recom.show()

# Print result
print recom

raw_input("...")
