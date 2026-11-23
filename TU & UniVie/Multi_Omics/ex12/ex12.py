
import pandas as pd


print("ex12.1")
data = pd.read_excel("/home/anton/Lectures/MultiOmics/ex12/Sheet_12/MK_Lipidomics.xlsx", index_col = "Species")

feature_map = data.drop(["Day", "Replicate"], axis = 1)

cleaned = feature_map.dropna(subset = ["Day0_1", "Day0_2", "Day0_3", "Day7_1", "Day7_2", "Day7_3"], how = "any", axis = 1)

#print(cleaned)


print("ex12.2")
from scipy import stats
import numpy as np
from statsmodels.stats.multitest import multipletests


day0 = cleaned.iloc[:3, :]
day7 = cleaned.iloc[9:13, :]

#print(day0, day7)


tStat, pValues = stats.ttest_ind(day0, day7, equal_var = False)

pValues_corr = multipletests(pValues, method = "fdr_bh")[1]
print(pValues, pValues_corr)

df_sig = cleaned.loc[:, pValues_corr <= 0.05]
print(df_sig.columns)

print("ex12.3")


sig_lipids = pValues_corr <= 0.05

count = len(sig_lipids)



print("ex12.4")
import matplotlib.pyplot as plt


plt.hist(pValues, bins = 50)
plt.show()


print("ex12.5")

x = np.log2(day7.mean() / day0.mean())
y = -np.log10(pValues_corr)
plt.xlabel("log2(fold change)")
plt.ylabel("-log10 (corr p-value)")
plt.title("Volcano Plot")

plt.scatter(x, y)
plt.show()