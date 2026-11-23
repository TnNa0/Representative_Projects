import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Exercise 8.1")

data = pd.read_excel("/home/anton/Lectures/MultiOmics/ex08/MK_Proteomics.xlsx")

row_names = []

for value in data.iloc[:, 0]:
    row_names.append(value)

#print(data.head(), data.describe(), row_names)


X = data.iloc[:, 2:]
y = data.iloc[:, 1]

print("Shape of X:", X.shape, "\n", y)


print("Exercise 8.2")


features = X.columns

print(X)
print(features)
x_norm = X.copy()

for feat in features:
    x_norm.loc[:, feat] = (X[feat] - X[feat].mean()) / X[feat].std()

print(x_norm.iloc[:, 0].mean(), x_norm.iloc[:, 0].std())

print("Exercise 8.3")

from sklearn.decomposition import PCA

pca = PCA()
components = pca.fit_transform(x_norm)

xx, yy = components[:, 0], components[:, 1]

vars = pca.explained_variance_ratio_

print("Exercise 8.4")

for val in sorted(set(y)):
    plt.scatter(xx[y == val], yy[y == val])
plt.xlabel("PC 1, Var: %0.2f%%" % (vars[0] * 100))
plt.ylabel("PC 2, Var: %0.2f%%" % (vars[1] * 100))
plt.legend()
plt.show()

print(y.unique())


print("Exercise 8.5")

m, x = 3, 0.85
reduced_components_a  = components[:, :m]

for p in range(1, components.shape[1] + 1):
    if sum(pca.explained_variance_ratio_[ : p]) > x: break
reduced_components_b = components[:, :p]

print("Method 1:", np.sum(pca.explained_variance_ratio_[:m]))
print("Method 2:", reduced_components_b.shape)