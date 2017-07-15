import sys
import os

# online
# F = sys.stdin

# froma file
fileName = "/stats0.1-2.txt"
F = open(os.path.dirname(__file__) + fileName, "r")

N = int(F.readline())
X = [int(s) for s in F.readline().split(" ")]
W = [int(s) for s in F.readline().split(" ")]
N = len(X)
weightedSum = 0
sumOfW = 0
for i in range(N):
    weightedSum = weightedSum + (X[i] * W[i])
    sumOfW = sumOfW + W[i]
weightedMean = weightedSum / sumOfW

print("{0:.1f}".format(weightedMean))
