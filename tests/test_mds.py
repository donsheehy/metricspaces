import unittest
from metricspaces.mds import MDS
from metricspaces import MetricSpace
from metricspaces.numpypoint import NumpyPoint as Point

class TestMDS(unittest.TestCase):
    def testinit(self):
        n = 9
        P = [Point((i,0,j,0)) for i in range(n) for j in range(n)]
        M = MetricSpace(P)
        MDS(M)

if __name__ == '__main__':
    unittest.main()
