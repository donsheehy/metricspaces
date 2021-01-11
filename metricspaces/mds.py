class MDS:
    def __init__(self, M, target_dimension = 2):
        """Initialize an empty MDS object for a given metric space M.
        """
        self.M = M
        n = len(M)

        # The matrix of squared distances
        D = np.array([[self.M.distsq(a,b) for a in self.M] for b in self.M])

        # B is the approximate covariance matrix.
        J = np.ones((n,n))
        I = np.identity(n)
        L = (I - J/n)
        B = (-0.5) * L @ D @ L

        # Compute the SVD
        U, Sigma, VT = np.linalg.svd(B)
        # Take the most significant directions (rescaled).
        Q = (U @ np.diag(Sigma ** (1/2)))[:,:target_dimension]
        # Compute the pseudoinverse.
        Q_dagger = (U @ np.diag((1/Sigma) ** (1/2)))

        # m = np.array([100,100,100,100])
        # delta_mu = (1/n) * sum(D[i] for i in range(n))
        # print(-1/2 * Q_dagger.T @ (m - delta_mu).T)


    def project(self, point):
        delta = [self.M.distsq(point, q) for q in self.M]
