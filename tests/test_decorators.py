from metricspaces import MetricSpace, R1
from metricspaces.decorators import metric_class
import unittest


class TestMetricClass(unittest.TestCase):
    def testmetricclass(self):
        @metric_class
        class MetricBall:
            def __init__(self, center, radius):
                self.center = center
                self.radius = radius

            def __contains__(self, point):
                dist = self.metric.dist
                return dist(self.center, point) <= self.radius

        M = MetricSpace(dist = R1.dist)
        Ball = MetricBall(M)
        B = Ball(5,3)
        self.assertTrue(2 in B)
        self.assertFalse(1 in B)


if __name__ == '__main__':
    unittest.main()
