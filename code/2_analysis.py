import pandas as pd
import matplotlib.pyplot as plt

print "[LOADING] train_triplets.txt..."
plays_header = ['userID','songID','plays']
plays_df = pd.read_csv('../csv/train_triplets.txt', sep='\t', names=plays_header)

# Total entries
total_entries = plays_df.count()[0]

# Percentage number of plays of songs
print "[CALCULATING] Percentage number of plays of songs..."
number_listens = []
for i in range(10):
	number_listens.append(float(plays_df.loc[plays_df['plays'] == i+1].count()[0])/total_entries*100)

# Show bar plot of the analysis
n = len(number_listens)
x = range(n) 
width = 1/1.5
plt.bar(x, number_listens, width, color="blue")
plt.xlabel("Plays")
plt.ylabel("Percentage")
plt.grid()
plt.savefig("../img/percentage_song_plays.png")
print "[SAVED] percentage_song_plays.png"
#plt.show()

