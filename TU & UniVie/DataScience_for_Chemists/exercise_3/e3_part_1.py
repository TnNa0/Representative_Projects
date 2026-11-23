from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans



"""
do agglomorativeclustering 
do again and set threshold
do again with different linker method ()
"""

def hirarchical(df, df_labels):
    """
    #single linkage
    clustering = AgglomerativeClustering(n_clusters=None, metric='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='single', 
                                     distance_threshold=0.7, compute_distances=True).fit(df)
    z=hierarchy.linkage(df,'single')
    hierarchy.dendrogram(z, labels=df_labels.values)
    plt.axhline(y=0.7, c='k', linestyle='--')
    plt.show()
    """

    #complete linkage
    clustering = AgglomerativeClustering(n_clusters=None, metric='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='complete', 
                                     distance_threshold=1.1, compute_distances=True).fit(df)
    z=hierarchy.linkage(df,'complete')
    hierarchy.dendrogram(z, labels=df_labels.values)
    plt.axhline(y=1.1, c='k', linestyle='--')
    plt.show()
    df_with_clusters = df.copy()
    df_with_clusters['cluster'] = clustering.labels_

    """
    #wards linkage
    clustering = AgglomerativeClustering(n_clusters=None, metric='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='average', 
                                     distance_threshold=1.2, compute_distances=True).fit(df)
    z=hierarchy.linkage(df,'average')
    hierarchy.dendrogram(z, labels=df_labels.values)
    plt.axhline(y=1.2, c='k', linestyle='--')
    plt.show()
    """

    return df_with_clusters

"""
find mean of each cluster = seed -> for kmean
do kmeans
"""

def kmean(df):
    # Compute initial centroids from hierarchical clusters
    initial_centroids = df.groupby('cluster').mean().drop('cluster', axis=1, errors='ignore').values

    # Use those as seeds for KMeans
    kmeans = KMeans(n_clusters=len(initial_centroids), init=initial_centroids, n_init=1)
    kmeans.fit(df.drop('cluster', axis=1))

    return kmeans.labels_, kmeans.cluster_centers_

def kmean_random(df):
    # Use random seeds for KMeans
    kmeans = KMeans(n_clusters=len(df.groupby('cluster')), init='random', n_init=10)
    kmeans.fit(df.drop('cluster', axis=1))

    return kmeans.labels_, kmeans.cluster_centers_
    

"""
first read file and process
.>handle NaN
.>handle non-numerical columns
.> & normalize
"""

df = pd.read_excel('./Exercise 3_data.xlsx')
df_labels = df['Unnamed: 0'] #save labels for labeling dendogram later
df_num_labels = df.drop(columns = 'Unnamed: 0') #drop object column
#print(df.head())
#print(df_num_labels.head())
#print(df_num_labels.dtypes)

df_num = df_num_labels.apply(pd.to_numeric, errors='coerce')#make numeric. problem was to read in object-first row

df_clean = df_num.dropna() #removes the entire row. makes completely comparable dataset
df_labels = df_labels.loc[df_clean.index] #get same indexing

#print(df_clean.head())
#print(df_clean.dtypes)

df_norm = ((df_clean - df_clean.min()) / (df_clean.max() - df_clean.min())) #min max normalization
#print(df_norm.head())


df_with_clusters = hirarchical(df_norm, df_labels)
kmeans_labels, centroids = kmean(df_with_clusters)
kmeans_labels_random, centroids_random = kmean_random(df_with_clusters)

# Add KMeans results back into DataFrame
df_with_clusters['kmeans_cluster'] = kmeans_labels
df_with_clusters['kmeans_random_cluster'] = kmeans_labels_random
df_with_clusters['Sample Name'] = df_labels.values  

# === Scenario 1: Seeded ===
print("=== Scenario 1: Seeded KMeans ===")
# Cluster centers (rounded for readability)
centers_seeded = pd.DataFrame(centroids, columns=df_norm.columns)
print("\nCluster Centers (Seeded):")
centers_seeded['sum'] = centers_seeded.sum(axis=1)
print(centers_seeded.round(3))

# Members per cluster
members_seeded = df_with_clusters[['Sample Name', 'kmeans_cluster']].sort_values('kmeans_cluster')
print("\nCluster Members (Seeded):")
print(members_seeded)

# === Scenario 2: Random ===
print("\n=== Scenario 2: Random KMeans ===")
centers_random = pd.DataFrame(centroids_random, columns=df_norm.columns)
centers_random['sum'] = centers_random.sum(axis=1)
print("\nCluster Centers (Random):")
print(centers_random.round(3))

members_random = df_with_clusters[['Sample Name', 'kmeans_random_cluster']].sort_values('kmeans_random_cluster')
print("\nCluster Members (Random):")
print(members_random)




"""
df_with_clusters['kmeans_cluster'] = kmeans_labels
print(df_with_clusters.groupby('kmeans_cluster').mean())

df_with_clusters['random_seeds_kmeans_cluster'] = kmeans_labels_random
print(df_with_clusters.groupby('kmeans_cluster').mean())
"""

"""

what i observed:
----------------

three different linkage methods were compared: single vs complete vs ward.
complete method was the most logical and detailed to me, compared to the others.
I chose a distanc ethreshold of 1.1, resulting in 8 clusters (2 sub clusters of RDI[except for unique RDI algae], 
2 clusters of BD20 & E10, 3 subclusters of E85 [while 2 clusters showed more similarity than the 3rd], 1 cluster of RDI algae)

the mean of all clusteres was computed and used as the centroid seed for kmeans clustering;
or random seeds were taken and iterated 10 times.

Finally, a matrix with normalized kmeans clustered values is returned which may be plotted using e.g. spider graph.
Also, each biofule is returned in a DF assigned to a cluster. 
When seeding based on hirarchical complete linkage - BD20 algae are part of cluster 0 together with other BD20.
This differs to random seeding, where - like in hirachical clustering - algae form their own cluster.

In the Cluster Center matrix in scenario 2 we observe for cluster 0 very bad scores(very high). Long distances and very toxic.
... how to comapre both scenarios further?
... trend in clustering?
-->analyze also within & between cluster distance. this might help to find which method, random or seeding would be better



"""