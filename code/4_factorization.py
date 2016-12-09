import sqlite3
import graphlab as gl

#Set Graphlab
gl.canvas.set_target('headless', port=7331)

# Load datasets
conn = sqlite3.connect('../sqlite/msd.sqlite3')
listens = gl.SFrame.from_sql(conn, "SELECT * FROM train where plays >=2")
listens.show()
raw_input("Press something to continue...")

# Build model
training_data, validation_data = gl.recommender.util.random_split_by_user(listens, 'userID', 'songID')
model = gl.recommender.create(training_data, 'userID', 'songID', target='plays')
model.show()
raw_input("Press something to continue...")

# Recommend songs to users
recommendations = model.recommend()
rmse_data = model.evaluate_rmse(validation_data, target='plays')

# Save & show the results
recommendations.save('../recommendations')
print recommendations.show()
print rmse_data
raw_input("Press something to continue...")
