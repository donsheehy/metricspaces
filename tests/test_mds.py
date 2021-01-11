import unittest
from metricspaces.mds import MDS
from metricspaces import MetricSpace
from metricspaces.np_point import NumpyPoint

class TestMDS(unittest.TestCase):
    def testinit(self):
        n = 15
        P = [NumpyPoint(1,2) for i in range(n)]


if __name__ == '__main__':
    unittest.main()
