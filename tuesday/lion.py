# for the test case that we looked at in class,
# paste the input
# 5 4 4
# 2 1 3
# 3 1 2
# 3 4 2
# 2 4 2
# and then hit Ctrl + Z
# and then hit Enter
# And you'll get the answer
# Use this link for an explanation of the problem and code from Grok, 
# https://x.com/i/grok/share/oraUxsX7YUuJAYnutEHisAiTw

import sys

input = sys.stdin.read
data = input().split()

idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1
k = int(data[idx]); idx += 1

lions = []
for i in range(k):
    r = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    lions.append((r, c, d, i+1))  # store 1-indexed id

counts = [0] * k

for j in range(k):
    rj, cj, _, _ = lions[j]
    for i in range(k):
        if i == j:
            continue
        ri, ci, di, _ = lions[i]
        if abs(ri - rj) + abs(ci - cj) <= di:
            counts[j] += 1

max_count = -1
best_idx = float('inf')

for j in range(k):
    if counts[j] > max_count:
        max_count = counts[j]
        best_idx = lions[j][3]
    elif counts[j] == max_count:
        best_idx = min(best_idx, lions[j][3])

print(best_idx, max_count)