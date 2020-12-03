from metricspaces import MetricSpace, R1
import unittest

class TestMetricSpace(unittest.TestCase):
    def testinit_empty(self):
        M = MetricSpace
    
    def testinit(self):
        n = 15
        P = [R1(i) for i in range(n)]
        M = MetricSpace(P)
        for j in range(n):
            for i in range(n-j):
                self.assertEqual(M.dist(P[i], P[i+j]), j)

    def testcaching(self):
        class TestPoint:
            def __init__(self):
                self.distances_computed = set()
            def dist(self, other):
                assert((self, other) not in self.distances_computed)
                self.distances_computed.add((self, other))
                return 0

        a, b, c = TestPoint(), TestPoint(), TestPoint()
        M = MetricSpace([a,b])
        self.assertEqual(M.dist(a, b), 0)
        with self.assertRaises(AssertionError):
            a.dist(b)
        # Reversing operands also hits the cache.
        self.assertEqual(M.dist(b, a), 0)
        # Other distances can still be computed.
        self.assertEqual(a.dist(c), 0)
        self.assertEqual(b.dist(c), 0)

    def test_dist_and_distsq(self):
        class TestPoint(float):
            def dist(self, other):
                return 2 * abs(self - other)

        a = TestPoint(4)
        b = TestPoint(5)
        c = TestPoint(9)
        M = MetricSpace([a,b,c])
        self.assertEqual(M.dist(a,b), 2)
        self.assertEqual(M.dist(a,c), 10)
        self.assertEqual(M.dist(c,a), 10)
        self.assertEqual(M.dist(a,b), 2) # still
        self.assertEqual(M.dist(c, b), 8)

        self.assertEqual(M.distsq(a,b), 4)
        self.assertEqual(M.distsq(a,c), 100)
        self.assertEqual(M.distsq(c,a), 100)
        self.assertEqual(M.distsq(a,b), 4) # still
        self.assertEqual(M.distsq(c, b), 64)


if __name__ == '__main__':
    unittest.main()
