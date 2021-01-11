# A Distance Matrix

Sometimes, especially in cases where distances have been precomputed offline, we might have the distances provided as matrix.
This is a sufficiently common situation that it might be better to provide some special mechanism for it.  For now, maybe try the following.

```python {cmd modify_source}
from metricspaces import MetricSpace

D = [[0, 30, 40], [30, 0, 50], [40, 50, 0]]

T = MetricSpace(dist = lambda x,y: D[x][y])
print(T.dist(1,2))
```
<!-- code_chunk_output -->

50


<!-- /code_chunk_output -->

One downside of this approach is that the cache will then duplicate all these distances.
If you can load the distances directly into a dictionary with frozenset pairs of points as keys, you can pass this directly to `__init__`.

```python {cmd modify_source}
from metricspaces import MetricSpace

D = [[0, 30, 40], [30, 0, 50], [40, 50, 0]]
my_cache = {frozenset((i,j)): D[i][j] for i in range(3) for j in range(i,3)}

T = MetricSpace(cache = my_cache)
print(T.dist(1, 2))
print(T.dist(2, 1))
```
<!-- code_chunk_output -->

50
50


<!-- /code_chunk_output -->
