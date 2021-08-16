# Multi-Dimensional Scaling (MDS) Explained

Multi-Dimensional Scaling is a technique for embedding data in Euclidean space.
The specific type of MDS relevant to metric spaces is **metric multi-dimensional scaling**.
The coordinates are chosen to minimize the sum of the squared error in the squared distances.
As is often the case, this kind of quadratic objective function is chosen because it both makes sense and also because it reduces to an eigenvector problem.

Here is a simple example in code.
We start with a metric space `M`.
For simplicity, we will use points that embed nicely into two dimensions, the vertices of a 3-4-5 triangle.

```python {cmd}
import numpy as np
from metricspaces import MetricSpace, NumpyPoint as Point

P = [Point((0,0)), Point((3,0)), Point((0,4))]
n = len(P)
M = MetricSpace(P)
```

```python {cmd continue}
D = np.array([[M.distsq(a,b) for a in P] for b in P])
```

Next, we compute the (approximate) covariance matrix `B`.
In the case of Euclidean points, the entries of `B` will correspond to dot products of the corresponding points.
That is, $B_{ij}$ will be equal to $p_i^\top p_j$.

```python {cmd continue}
J = np.ones((n,n))
I = np.identity(n)
L = (I - J/n)
B = (-1.0/2) * L @ D @ L
```

The change of basis matrix `L` is a symmetric projection matrix along the all ones vector.
Just as in Principle Component Analysis, the eigenvectors of the covariance matrix give the desired embedding.
We extract these using the singular value decomposition of `B` as follows.

```python {cmd continue}
target_dimension = 2
U, Sigma, VT = np.linalg.svd(B)
Q = (U @ np.diag(Sigma ** (1/2)))[:,:target_dimension]
```

The matrix `Q` then gives the embedded points.
Below, we print their coordinates and the pairwise distances.

```python {cmd continue}
print("The normalized eigenvectors:")
print(Q)
print("The pairwise distances:")
print(M.dist(Point(Q[0]),Point(Q[1])))
print(M.dist(Point(Q[0]),Point(Q[2])))
print(M.dist(Point(Q[2]),Point(Q[1])))
```

Note that there is a slight numerical error in the output.
This is not uncommon given the numerical algorithms required to compute the eigenvectors.
