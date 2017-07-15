import sys
import os


def median(X):
    n = len(X)
    X.sort()
    medianIndex = int(n/2)
    median = 0
    if n % 2 == 0:
        median = (X[medianIndex]+X[medianIndex-1])/2
    else:
        median = X[medianIndex]
    return int(median)

#f = sys.stdin
fileName = "/stats1.txt"
f = open(os.path.dirname(__file__) + fileName, "r")

n = int(f.readline())
X = [int(x) for x in f.readline().split(" ")]
q2 = median(X)
H1 = []
H2 = []
if n % 2 == 0:
    m = int(n/2)
    for i in range(m):
        H1.append(X[i])
    for i in range(m, n):
        H2.append(X[i])
else:
    m = int(n/2)
    for i in range(m):
        H1.append(X[i])
    for i in range(m+1, n):
        H2.append(X[i])

q1 = median(H1)
q3 = median(H2)
print(q1)
print(q2)
print(q3)
