import graphlab as gl
import sqlite3
from graphlab import SFrame as sf

# Load dataset
print "[LOADING] data"
conn = sqlite3.connect('../sqlite/msd.sqlite3')
data= gl.SFrame.from_sql(conn, "SELECT * FROM train")

# Create Training set and test set
train_data, test_data = gl.recommender.util.random_split_by_user(data, 'userID', 'songID')

# Create the model
model = gl.recommender.create(train_data, 'userID', 'songID', target='plays', ranking = False)

# Recommend to users
recom = model.recommend()

# Evaluate the model
rmse_data = model.evaluate_rmse(test_data, target='plays')

# Show results
recom.show()

# Print result
print recom

# Print evaluation
print rmse_data

raw_input("...")
