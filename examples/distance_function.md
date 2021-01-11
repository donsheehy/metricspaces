# A Distance Function

One of the simplest way to express a metric is to define the distance directly as a function.

Let's write a function that computes the hamming distance between strings.
The distance between strings of the same length is the number of indices at which the strings differ.
If the lengths differ, the distance is increased by the difference of the lengths.

```python {cmd id="distance"}
def hamming_distance(a, b):
    length_difference = abs(len(a) - len(b))
    return length_difference + sum(1 for s,t in zip(a,b) if s != t)
```

Here are a couple examples to see if it works.

```python {cmd continue="distance" modify_source}
print(hamming_distance("aaa", "aab")) # should be 1
print(hamming_distance("aaa", "abb")) # should be 2
print(hamming_distance("aaa", "abbxxx")) # should be 5
```
<!-- code_chunk_output -->

1
2
5


<!-- /code_chunk_output -->


Here is how you would construct a metric space that uses this function to compute distances.

```python {cmd continue="distance"}
from metricspaces import MetricSpace

S = MetricSpace(dist = hamming_distance)
```
It's necessary to use the named parameter `dist` in order to pass the distance function.
The first positional parameter would be a collection of points, but it is optional.
Here it is in action.

```python {cmd continue modify_source}
print(S.dist("aaa", "aab")) # should be 1
print(S.dist("aaa", "bac")) # should be 2
```
<!-- code_chunk_output -->

1
2


<!-- /code_chunk_output -->
