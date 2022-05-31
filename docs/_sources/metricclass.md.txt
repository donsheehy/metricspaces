# The Metric Class Decorator

Sometimes, you will write a class that needs to compute distances.
This means that it ought to have access to the metric space object and not just the points.
A simple example would be a class for a metric ball like the following.

```python
class MetricBall:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __contains__(self, point):
        return self.center.dist(point) <= self.radius
```

This code will work just fine in many cases, but it will fail if the metric has been specified by a distance function that is not a method on the points.
It will also bypass the cache.

One cumbersome solution would be to store the metric space in the ball object.
This is highly redundant if there are many balls.
A second solution would be to store the metric space as an attribute of the class.
The problem with this solution is that it would only permit one kind of metric ball to exist at a time.
A third solution would be to subclass `MetricBall` and then assign the metric as an attribute of the subclass.
At first, this seems the most cumbersome to write, even if it resolves the main issues and corresponds precisely to what we want the class to mean, i.e., it is a metric ball in a particular metric.
As this pattern is relatively standard, we provide a decorator that makes it trivial to produce subclasses this way.
This is how you would write the same `MetricBall` class with the decorator.

```python
@metric_class
class MetricBall:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __contains__(self, point):
        dist = MetricBall.metric.dist
        return dist(self.center, point) <= self.radius
```

The only line of code that is different is that we are now accessing the metric via an attribute called `metric` that is defined on the class.
To use this class, we would first define the type by combining a metric space and a metric ball as follows.

```python
M = MetricSpace()
Ball = MetricBall(M)
ball = Ball((0,0), 1)
```

The point here is the decorator turns the `MetricBall` class into a function that returns a class.
The `MetricSpace` is a parameter to this function.

If you define a new class this way, you may wish to assign the name of the class manually.
Looking at the type of `ball` above, we would not see `Ball`, but instead `MetricBall_M`.
If you want to also change the name, you can give a second parameter with the name when defining the `Ball` class as follows.

```python
Ball = MetricBall(M, "Ball")
```
