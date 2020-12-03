class MetricSpace:
    def __init__(self, points = (), dist = None, cache = None):
        """
        Initialize a new `MetricSpace` object.

        The `points` and the `dist` function are optional.
        If `dist` is not provided, then the distance is computed by calling
        the `dist` method on the point.

        It is possible to seed the cache at the time of construction.
        If `cache` is not provided, a new empty cache will be initialized.
        """
        self.cache = cache if cache is not None else {}
        self.points = set(points)
        self.distfn = dist if dist is not None else MetricSpace.pointdist

    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)

    def pointdist(a, b):
        """
        Return the distance from `a` to `b` as measured using the metric
        supplied by the input points.
        """
        return a.dist(b)

    def dist(self, a, b):
        """
        Return the distance from`a` to `b`.

        The metric used will depend on the `distfn`.
        """
        key = frozenset((a,b))
        if key not in self.cache:
            self.cache[key] = self.distfn(a,b)
        return self.cache[key]

    def distsq(self, a, b):
        """
        Return the squared distance from `a` to `b`.
        """
        return self.dist(a, b) ** 2.

    def comparedist(self, x, a, b, delta = 0):
        """
        Return True iff `x` is closer to `a` than to `b`.

        Technically, it returns `d(x,a) < d(x,b) - delta`, where delta is
        optional and defaults to zero.
        """
        return self.dist(x,a) < self.dist(x,b) - delta

    def distlt(self, a, b, delta = 0):
        """
        Return True iff `d(a,b) < delta`.
        """
        return self.dist(a,b) < delta
