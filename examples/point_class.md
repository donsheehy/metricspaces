# A Point Class

Another common way to define a metric would be to define a metric as a method on an object.

```python {cmd id="pointclass"}
class MyPoint:
    def __init__(self, x):
        self.x = x

    def dist(self, other):
        return abs(self.x - other.x)
```

```python {cmd continue}
from metricspaces import MetricSpace

P = MetricSpace()
```

```python {cmd continue modify_source}
a = MyPoint(4)
b = MyPoint(8)
print(P.dist(a, b))
```
<!-- code_chunk_output -->

4


<!-- /code_chunk_output -->

**Wait!  WAT?**

You might be wondering how this got glued together.
There was nothing in the instantiation of the `MetricSpace` object that indicated the type of the points.
This is fine.
In the absence of other info, the class defaults to look for a `dist` method on the points.

You could also have done the following, but there is not a good reason to do so.

```python {cmd continue="pointclass" modify_source}
from metricspaces import MetricSpace

P = MetricSpace(dist = MyPoint.dist)
print(P.dist(MyPoint(3), MyPoint(5))) # should be 2
```
<!-- code_chunk_output -->

2


<!-- /code_chunk_output -->

One case where you might want to pass a distance method explicitly is if it has a name other than `dist`.
This can be useful for wrangling your distance into a `MetricSpace` object.
Here is an example.

```python {cmd modify_source}
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

2


<!-- /code_chunk_output -->

If you are uncomfortable passing a method name to a function, then I would encourage you to seize this moment to really embrace that it's just a function.
It only becomes a method when called on an object.
This is yet another reason why including `self` explicitly as a parameter is a brilliant design decision... but I digress.
