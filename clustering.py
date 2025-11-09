import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

class KMeans:
    def __init__(self, n_clusters, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters

    def fit(self, X):
        # Set seed for reproducibility
        np.random.seed(42)
        
        # Initialize centroids randomly from the data points
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iters):
            # Assign each data point to the nearest centroid
            labels = self._assign_labels(X)

            # Compute new centroids
            new_centroids = self._update_centroids(X, labels)

            # Check for convergence
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def _assign_labels(self, X):
        # Compute distances from each data point to each centroid
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        # Assign labels based on the closest centroid
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        # Calculate the mean of all points assigned to each cluster
        return np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])


# Generate synthetic data with 3 cluster centers
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)

# Create and fit the KMeans model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Get the final cluster assignments
labels = kmeans._assign_labels(X)

# Print results
print("Cluster Assignments:", labels)
print("Final Centroids:\n", kmeans.centroids)

# Optional: Plotting the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, alpha=0.6)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.legend()
plt.show()
