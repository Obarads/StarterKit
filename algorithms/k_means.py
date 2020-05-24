def create_distribution(n_samples=1500, random_state=170):
    # https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py
    from sklearn.datasets import make_blobs
    X, y = make_blobs(n_samples=n_samples, random_state=random_state)
    return X, y

def imp_cupy():
    import cupy as cp

def imp_numpy(X, y, k, max_iter=100):
    import numpy as np
    centers = np.random.random_sample((3,2))
    for i in range(max_iter):
        dist = []
        for center in centers:
            dist.append(X - center)
        dist = np.array(dist)
        


def main():
    import matplotlib.pyplot as plt

    X, y = create_distribution()
    k = 3
    # Incorrect number of clusters
    imp_numpy(X, y, k)


if __name__ == "__main__":
    main()