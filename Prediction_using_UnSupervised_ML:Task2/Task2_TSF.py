#Task-2 of TSF internship
#======================================================================
#From the given ‘Iris’ dataset, predict the optimum number of clusters and represent it visually.
#======================================================================

#Linkedin Id : https://www.linkedin.com/in/meet-patel-8896561b6/



'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# --> Importing the essential modules
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# --> Import the Iris dataset
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

iris_data = datasets.load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
#print only first 5 rows
print(iris_df.head())

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# --> Finding the optimal number of clusters for K-means and determining the value
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

x = iris_df.iloc[:, [0,1,2,3]].values
within_cluster_sum_squares = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    within_cluster_sum_squares.append(kmeans.inertia_)
#You can print list that we have created to see
#print(within_cluster_sum_squares)
#plot the graph to observe what we are doing above
plt.plot(range(1, 11), within_cluster_sum_squares)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('within_cluster_sum_squares')
plt.show()

'''
Note : The elbow method" got its name from the elbow pattern forming something like above. The optimal clusters are formed where the elbow occurs. This is when the WCSS(Within Cluster Sum of Squares) doesn't decrease with every iteration significantly.

       Here we taken the number of clusters as '3'.
'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# --> Creating a KMeans classifier
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Apply KMeans to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# --> Now turn to Visualizing the cluster data
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#on first 2 columns
plt.scatter(x[y_kmeans == 0,0], x[y_kmeans == 0,1], s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1,0], x[y_kmeans == 1,1], s = 100, c = 'orange', label = 'Iris-versicolor')
plt.scatter(x[y_kmeans == 2,0], x[y_kmeans == 2,1], s = 100, c = 'yellow', label = 'Iris-virginica')

#plot the centroid of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'black', label = 'Centroids')
plt.legend()
plt.show()

#By Meet Patel
