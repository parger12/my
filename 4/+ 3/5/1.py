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

for row in spot_matrix:
    for value in row:
        if value in spot_counts:
            spot_counts[value]  += 1
        else:
            spot_counts[value] = 1

spot_probs = {}

for key in spot_counts:
    spot_probs[key] = spot_counts[key]/36

print(spot_counts)

