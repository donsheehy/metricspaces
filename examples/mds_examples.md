# MDS examples

Let's define a collection of points that are near a plane in 4D.

```python {cmd}
from metricspaces import MetricSpace
from metricspaces import NumpyPoint as Point
from random import randrange
from numpy import array

# def affine(x,y):
#     return Point([x, y, 10 * x + 3 * y + 12 + randrange(5000), 4 * x + 2 * y])
def affine(x,y):
    return Point([x, y, randrange(50)])

n = 100
P = [Point(affine(randrange(10 * n), randrange(10 * n))) for _ in range(n)]

M = MetricSpace(P)
```

Now we can compute the MDS embedding into 2D and look at the largest distortion

```python {cmd continue}
from metricspaces.mds import MDS

def distortion(A,B, i, j):
    if i == j:
        return 1
    return max(B[i].dist(B[j]) / A[i].dist(A[j]),
    A[i].dist(A[j]) / B[i].dist(B[j]))

embedding = MDS(M,2).metricspace()
X = list(embedding)

i,j = 2,5

print(f"X[i] = {X[i]} \nX[j] = {X[j]}\nX[i].dist(X[j]) = {X[i].dist(X[j])}")
print(f"P[i] = {P[i]} \nP[j] = {P[j]}\nP[i].dist(P[j]) = {P[i].dist(P[j])}")


d = [distortion(P, X, i, j) for i in range(n) for j in range(n)]
# print(embedding.dist(X[3], X[4]))
# print(M.dist(P[3], P[4]))
print(max(d))
```
