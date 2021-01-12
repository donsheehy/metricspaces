# Examples

## A Distance Function

One of the simplest way to express a metric is to define the distance directly as a function.

Let's write a function that computes the hamming distance between strings.
The distance between strings of the same length is the number of indices at which the strings differ.
If the lengths differ, the distance is increased by the difference of the lengths.

```python
def hamming_distance(a, b):
    length_difference = abs(len(a) - len(b))
    return length_difference + sum(1 for s,t in zip(a,b) if s != t)
```

Here are a couple examples to see if it works.

```python
print(hamming_distance("aaa", "aab")) # should be 1
print(hamming_distance("aaa", "abb")) # should be 2
print(hamming_distance("aaa", "abbxxx")) # should be 5
```
<!-- code_chunk_output -->

```
1
2
5
```

<!-- /code_chunk_output -->


Here is how you would construct a metric space that uses this function to compute distances.

```python
from metricspaces import MetricSpace

S = MetricSpace(dist = hamming_distance)
```
It's necessary to use the named parameter `dist` in order to pass the distance function.
The first positional parameter would be a collection of points, but it is optional.
Here it is in action.

```python
print(S.dist("aaa", "aab")) # should be 1
print(S.dist("aaa", "bac")) # should be 2
```
<!-- code_chunk_output -->
```
1
2
```

<!-- /code_chunk_output -->

## A Point Class

Another common way to define a metric would be to define a metric as a method on an object.

```python
class MyPoint:
    def __init__(self, x):
        self.x = x

    def dist(self, other):
        return abs(self.x - other.x)
```

```python
from metricspaces import MetricSpace

P = MetricSpace()
```

```python
a = MyPoint(4)
b = MyPoint(8)
print(P.dist(a, b))
```
<!-- code_chunk_output -->
```
4
```

<!-- /code_chunk_output -->

**Wait!  WAT?**

You might be wondering how this got glued together.
There was nothing in the instantiation of the `MetricSpace` object that indicated the type of the points.
This is fine.
In the absence of other info, the class defaults to look for a `dist` method on the points.

You could also have done the following, but there is not a good reason to do so.

```python
from metricspaces import MetricSpace

P = MetricSpace(dist = MyPoint.dist)
print(P.dist(MyPoint(3), MyPoint(5))) # should be 2
```
<!-- code_chunk_output -->
```
2
```

<!-- /code_chunk_output -->

One case where you might want to pass a distance method explicitly is if it has a name other than `dist`.
This can be useful for wrangling your distance into a `MetricSpace` object.
Here is an example.

```python
from metricspaces import MetricSpace

class MyOtherPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def l_infinity(self, other):
        return max(abs(other.x - self.x), abs(other.y - self.y))

L_inf = MetricSpace(dist = MyOtherPoint.l_infinity)

a = MyOtherPoint(2,6)
b = MyOtherPoint(3,4)
print(L_inf.dist(a,b)) # should be 2
```
<!-- code_chunk_output -->
```
2
```


<!-- /code_chunk_output -->

If you are uncomfortable passing a method name to a function, then I would encourage you to seize this moment to really embrace that it's just a function.
It only becomes a method when called on an object.
This is yet another reason why including `self` explicitly as a parameter is a brilliant design decision... but I digress.

## A Distance Matrix

Sometimes, especially in cases where distances have been precomputed offline, we might have the distances provided as matrix.
This is a sufficiently common situation that it might be better to provide some special mechanism for it.  For now, maybe try the following.

```python
from metricspaces import MetricSpace

D = [[0, 30, 40], [30, 0, 50], [40, 50, 0]]

T = MetricSpace(dist = lambda x,y: D[x][y])
print(T.dist(1,2))
```
<!-- code_chunk_output -->
```
50
```

<!-- /code_chunk_output -->

One downside of this approach is that the cache will then duplicate all these distances.
If you can load the distances directly into a dictionary with frozenset pairs of points as keys, you can pass this directly to `__init__`.

```python
from metricspaces import MetricSpace

D = [[0, 30, 40], [30, 0, 50], [40, 50, 0]]
my_cache = {frozenset((i,j)): D[i][j] for i in range(3) for j in range(i,3)}

T = MetricSpace(cache = my_cache)
print(T.dist(1, 2))
print(T.dist(2, 1))
```
<!-- code_chunk_output -->
```
50
50
```

<!-- /code_chunk_output -->
