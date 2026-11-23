import pandas as pd
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

print("Exerise 9.1")
data = pd.read_excel("/home/anton/Lectures/MultiOmics/ex09/Sheet_09/MK_Proteomics.xlsx")

data_num = data.iloc[:, 2:]
features = data_num.columns

print(data.head())
print("number of days sampled:", len(data.iloc[:, 1].unique()))
#print(data_num.head())
#print(features)

data_norm = data_num.copy()

for feat in features:
    data_norm.loc[:, feat] = (data[feat] - data[feat].mean()) / data[feat].std()

print(data_norm.iloc[:, 0].mean(), data_norm.iloc[:, 0].std())

lkg = hierarchy.linkage(data_norm, method = 'average', metric = 'euclidean')
dn = hierarchy.dendrogram(lkg)
plt.show()

cluster_index = hierarchy.fcluster(lkg, t=80, criterion = 'distance')

clusters = {c: [] for c in set(cluster_index)}
for i, c in enumerate(cluster_index): clusters[c].append(i)

print(clusters)


print("Exerise 9.2")
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, random_state = 100)
kmeans.fit(data_norm)
print(kmeans.labels_)


print("Exerise 9.3")

xt = PCA().fit_transform(data_norm)[:, :2]

kmeans = KMeans(n_clusters = 3, random_state = 100)
kmeans.fit(xt)
print(kmeans.labels_)

plt.scatter(xt[:, 0], xt[:, 1], c = kmeans.labels_)
plt.show()