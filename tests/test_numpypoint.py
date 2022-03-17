from metricspaces.numpypoint import NumpyPoint, L_p
import unittest

class TestNumpyPoint(unittest.TestCase):
    def testsimplecase(self):
        p = NumpyPoint((0,0))
        q = NumpyPoint((3,4))
        self.assertEqual(p.distsq(q), 25)
        self.assertEqual(p.dist(q), 5)

    def testpointsarehashable(self):
        hash(NumpyPoint([2,3,4]))

    def testdistsq(self):
        a = NumpyPoint((1,2,3))
        b = NumpyPoint((2,3,1))
        self.assertEqual(a.distsq(b), 6)

    def testpointsareiterable(self):
        p = NumpyPoint((2,4,6,8))
        self.assertEqual(list(p), [2,4,6,8])

class TestL_pNorms(unittest.TestCase):
    def testL_1_simple(self):
        P = L_p(1)
        a = P([1,2,3])
        b = P([2,3,4])
        c = P([0,0,0])
        self.assertEqual(a.dist(b), 3)
        self.assertEqual(b.dist(a), 3)
        self.assertEqual(c.dist(a), 6)
        self.assertEqual(a.dist(c), 6)

    def testL_inf_simple(self):
        P = L_p('inf')
        a = P([2,7])
        b = P([1,12])
        c = P([12, 4])
        self.assertEqual(a.dist(b), 5)
        self.assertEqual(b.dist(a), 5)
        self.assertEqual(c.dist(a), 10)
        self.assertEqual(a.dist(c), 10)

if __name__ == '__main__':
    unittest.main()
