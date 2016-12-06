import graphlab as gl
from graphlab import SFrame as sf
import pandas as pd

# Load datasets

plays_header = ['user_id','item_id','rating']

print "[LOADING] train_triplets"

df= pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

data=sf(data=df)

model = gl.item_similarity_recommender.create(data, target="rating",similarity_type='pearson')

prediction= model.predict(data);

#evaluation = gl.item_similarity_recommender.

recommendation= model.recommend();

recommendation.save('../similarities')



print recommendation