#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# mean, median and mode
# by Gracky

import os

fileName = "/stats0.txt"
f = open(os.path.dirname(__file__) + fileName, "r")
# use this open, and f.readLine() instead of input()

n = int(f.readline())
X = [int(s) for s in f.readline().split(" ")]

mean = 0
for x in X:
    mean = mean+x
mean = mean/n
print(mean)

X.sort()
medianIndex = int(n/2)
median = 0
if n % 2 == 0:
    median = (X[medianIndex]+X[medianIndex-1])/2
else:
    median = X[medianIndex]
print(median)

biggestCountWeaveSeenSoFar=0
mode = 0
for x in X:
    c = X.count(x)
    if c > biggestCountWeaveSeenSoFar:
        biggestCountWeaveSeenSoFar=c
        mode = x
print(mode)
