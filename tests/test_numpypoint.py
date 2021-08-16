from metricspaces.numpypoint import NumpyPoint
import unittest

class TestNumpyPoint(unittest.TestCase):
    def testsimplecase(self):
        p = NumpyPoint((0,0))
        q = NumpyPoint((3,4))
        self.assertEqual(p.distsq(q), 25)
        self.assertEqual(p.dist(q), 5)

    def testpointsarehashable(self):
        hash(NumpyPoint([2,3,4]))

if __name__ == '__main__':
    unittest.main()
