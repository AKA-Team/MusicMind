import graphlab as gl
import sqlite3
from graphlab import SFrame as sf

# Load dataset
print "[LOADING] data"
conn = sqlite3.connect('../sqlite/msd.sqlite3')
item_data = gl.SFrame.from_sql(conn, "SELECT * FROM song LIMIT 1000")

# Create Training set and test set
#train_data, test_data = gl.recommender.util.random_split_by_user(item_data, 'songID')

# Create the model
model = gl.recommender.item_content_recommender.create(item_data, 'songID')

# Recommend to users
recom = model.recommend()

# Show results
model.show()

# Print result
#print recom

raw_input("...")
