import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print "[LOADING] train_triplets..."
plays_header = ['userID','songID','plays']
plays_df = pd.read_csv('../csv/train_triplets.csv', sep='\t', names=plays_header)

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
plt.xlabel("Plays"); plt.ylabel("%")
plt.title("Percentage number of plays of songs")
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.savefig("../img/percentage_song_plays.png")
print "[SAVED] percentage_song_plays.png"
#plt.show()
plt.clf()

# Cumulative sum
cumsum_listens = np.cumsum(number_listens)
cumsum_listens = np.insert(cumsum_listens, 0, 0)
plt.plot(np.linspace(0,10,11),cumsum_listens)
plt.xticks(np.linspace(0,10,11), np.linspace(0,10,11))
plt.xlabel("Number of Plays"); plt.ylabel("Cumulative sum")
plt.title("Cumulative disribution of Number of Song Plays")
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.savefig("../img/cumulative_sum.png")
print "[SAVED] cumulative_sum.png"
#plt.show()
