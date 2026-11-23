import pandas as pd
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy
import seaborn as sns
import matplotlib.colors as mcolors

print("Ex10.1")

# def moving_average_smoothing(x, y, window_width):
#     x, y = np.array(x), np.array(y)
#     y_new, st, en, n, hw = [], 0, 0, len(x), window_width / 2
#     for i in range(n):
#         while st < n - 1 and x[i] - x[st] > hw: st += 1
#         while en < n - 1 and x[en] - x[i] <= hw: en += 1
#         y_new.append(sum(y[st : en]) / (en - st + 1))
#     return np.array(y_new)


# covid = pd.read_excel("/home/anton/Lectures/MultiOmics/ex10/Sheet_10/covid-data.xlsx", index_col = "location").astype(float)
# for i, row in covid.iterrows():
#     covid.loc[i] = moving_average_smoothing(range(len(row)), row, 7)


# lkg = hierarchy.linkage(covid, method = "average", metric = "cosine")
# clusters = hierarchy.fcluster(lkg, t = 0.25, criterion = "distance")

# colors = [v for k, v in mcolors.TABLEAU_COLORS.items()]
# group_colors = [colors[c % len(colors)] for c in clusters]

# D = pdist(covid, "cosine")
# S = 1 - squareform(D)

# #labels_sorting = hierarchy.leaves_list(lkg)
# #S = S[labels_sorting]
# #S = S[:, labels_sorting]

# cm = pd.DataFrame(S, index = covid.index, columns = covid.index)
# sns.clustermap(cm, row_linkage = lkg, col_linkage = lkg, cmap = "bwr", vmin = -1, vmax = 1, row_colors = group_colors)

# plt.show()

print("Ex10.2")


df_input = pd.read_excel("/home/anton/Lectures/MultiOmics/ex10/Sheet_10/MK_Proteomics.xlsx")
df_t = df_input.iloc[:, 2:].T
print(df_t)

print("Ex10.3")

df = pd.DataFrame(index = df_t.index)

df["Day0"] = df_t.iloc[:, 0:3].mean(axis=1)
df["Day1"] = df_t.iloc[:, 3:6].mean(axis=1)
df["Day3"] = df_t.iloc[:, 6:9].mean(axis=1)
df["Day7"] = df_t.iloc[:, 9:12].mean(axis=1)

print(df)

print("Ex10.4")

lkg = hierarchy.linkage(df, method = "average", metric = "cosine")

clusters = hierarchy.fcluster(lkg, t = 0.001, criterion = "distance")

groups = {c: [] for c in set(clusters)}
for i, c in enumerate(clusters): groups[c].append(i)

c = 0
for k, v in groups.items():
    if len(v) >= 20:
        c += 1
        print(k, len(v), [df.index[i] for i in v])
        print("clusters:", c)

plt.show()

print("Ex10.5")
