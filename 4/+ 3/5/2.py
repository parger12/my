import numpy as np

spot_matrix = np.array(
    [
        [10, 11, 12, 13, 14, 15],
        [11, 12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16, 17],
        [13, 14, 15, 16, 17, 18],
        [14, 15, 16, 17, 18, 19],
        [15, 16, 17, 18, 19, 20],
    ]
)

spot_counts = {}
for i in range(0, 6):
    for j in range(0, 6):
        if spot_matrix[i][j] not in spot_counts.keys():
            spot_counts[spot_matrix[i][j]] = 1
        else:
            spot_counts[spot_matrix[i][j]] += 1

spot_probs = {k:spot_counts[k]/36 for k in spot_counts}
print(spot_probs)

sum_probs_one = round(sum(spot_probs.values()), 2)

print (sum_probs_one)