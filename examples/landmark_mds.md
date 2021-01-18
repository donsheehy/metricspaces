# Landmark MDS

De Silva and Tenenbaum introduced a variant of multidimensional scaling that works by using a subset of points called landmarks.
The other points are all placed with respect to their distance to these landmarks.

Let $p_0,\ldots, p_d$ be the landmarks.
The first step is to find an embedding of these points into $\R^d$ using MDS.
Let  $q_0,\ldots, q_d$ denote the embedded points in $\R^d$.
For a new point $x$ to be embedded as $y$ in $\R^d$, we would like its distance to the landmarks to be preserved by the embedding.
That is, we want that for all $i\in [d+1]$,
\[
  \|y-q_i\| = d(x, p_i).
\]
An equivalent formulation that avoids square roots is to instead try to satisfy
\[
  \|y-q_i\|^2 = d(x, p_i)^2.
\]
We are trying to solve for $y$, so one way to eliminate the quadratic term in $y$ is to exploit the fact that the landmarks have mean zero (this is a property of the MDS that embedded them).
\[
  \begin{aligned}
  \|y-q_i\|^2 - \frac{1}{d+1}\sum_j\|y-q_j\|^2
    &= -2q_i^\top y + \|q_i\|^2 - \frac{1}{d+1}\sum_j(-2q_j^\top y + \|q_j\|^2)\\
    &= -2q_i^\top y + \|q_i\|^2 - \frac{-2}{d+1}y^\top(\sum_j q_j) - \frac{1}{d+1}\sum_j \|q_j\|^2\\
    &= -2q_i^\top y + \|q_i\|^2 - \frac{1}{d+1}\sum_j \|q_j\|^2\\
  \end{aligned}
\]


\[
  -2q_i^\top y = d(x,p_i)^2 - \|q_i\|^2 + -\frac{1}{d+1}\sum_j(\|q_j\|^2 - d(x,p_j)^2)
\]
Notice that everything on the right side is known and the last term, $\frac{1}{d+1}\sum_j(\|q_j\|^2 - d(x,p_j)^2)$, does not depend on $i$.
We can package these into a single linear system as follows using the vectors
\[
  \delta_x = \begin{bmatrix}
    d(x, p_0)^2\\ \vdots\\ d(x, p_d)^2
    \end{bmatrix},~~~
  s = \begin{bmatrix}
    \|q_0\|^2\\ \vdots\\ \|q_d\|^2
    \end{bmatrix},~\text{and}~~
  \mathbf{1} = \begin{bmatrix}
    1\\ \vdots\\ 1
    \end{bmatrix}.
\]
Letting $Q$ be the matrix with rows $q_i$, this yields the system
\[
  -2Q y = \delta_x - s - \left(\frac{1}{d+1}\sum_j(\|q_j\|^2 - d(x,p_j)^2)\right)\mathbf{1}
\]
This system may not have a solution in general, but we can take the pseduoinverse $Q^\dagger$ of $Q$ and compute $y$ as
\[
  y = - \frac{1}{2}Q^\dagger\left(\delta_x - s - \left(\frac{1}{d+1}\sum_j(\|q_j\|^2 - d(x,p_j)^2)\right)\mathbf{1}\right)
\]
Recall that the kernel of the pseudoinverse is equal to the kernel of the transpose.
In particular, because the mean of the $q_i$s is zero, we have $Q^T\mathbf{1} = 0$, so we can cancel out the last term in our linear system, leaving us with
\[
  y = - \frac{1}{2}Q^\dagger\left(\delta_x - s\right)
\]

## Coding it up

We can proceed exactly as in the MDS example.

```python {cmd}
import numpy as np
from metricspaces import MetricSpace, NumpyPoint as Point

P = [Point((0,0)), Point((3,0)), Point((0,4))]
n = len(P)
M = MetricSpace(P)

D = np.array([[M.distsq(a,b) for a in P] for b in P])
L = (np.identity(n) - np.ones((n,n))/n)
B = (-1.0/2) * L @ D @ L
U, Sigma, VT = np.linalg.svd(B)
Q = (U @ np.diag(Sigma ** (1/2)))
```

The rows of `Q` give the desired embedding.
The pseudo-inverse of `Q` can be computed directly from the SVD as follows.

```python {cmd continue id="qdagger"}
Q_dagger = (U @ np.diag((1/Sigma) ** (1/2))).T
```

Now, we can add another point.

```python {cmd continue="qdagger"}
x = Point((3,4))

delta_x = np.array([M.distsq(x,p) for p in P])
delta_mu = (1/n) * sum(D[i] for i in range(n))
s = np.array([np.dot(Q[i], Q[i]) for i in range(n)])
y = -1/2 * Q_dagger @ (delta_x - s).T
y = -1/2 * Q_dagger @ (delta_x - delta_mu).T
print(y)
print(M.dist(Point(y), Point(Q[0])))
```

Clearly something went terribly wrong.
The problem here is the numerical instability of the (nearly) zero coordinates in the embedding $Q$.
These get blown up into huge coordinates in the pseduoinverse.
If we were to project them out first, we get much more reasonable results.

```python {cmd continue="qdagger"}
x = Point((3,4))

dim = 2
Q = Q[:,:dim]
delta_x = np.array([M.distsq(x,p) for p in P])
s = np.array([np.dot(Q[i], Q[i]) for i in range(n)])
y = (-1/2 * Q_dagger @ (delta_x - s).T)[:dim]
print(y)
print(M.dist(Point(y), Point(Q[0])))
print(M.dist(Point(y), Point(Q[1])))
print(M.dist(Point(y), Point(Q[2])))
```

This is much better.
