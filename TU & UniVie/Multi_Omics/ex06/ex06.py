import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
Exercise 6.1 (3 points)
We set up an experiment where we measured the insulin concentratition for 10 different persons on three different day
times (morning, afternoon, evening) points on two different spots (skin, plasma). Your will find a table file attached to
this document. The table is stored in long table format. Transform it as a pivot table where the Person column is the
index, the Day time and Sample source columns form a multi-column index, and the Insulin value column is the value
column. Print the pivot table in the console for control.
Hint: to create multi-row or multi-column indexes, you can define several columns in a list as the index or columns
parameter.
'''
exp = pd.read_excel("/home/anton/Lectures/MultiOmics/ex06/Sheet_06/Insulin-Experiment.xlsx")
print("Shape:\n", exp.shape, "\nHead:\n", exp.head(), "\nDescription:\n", exp.describe())
print(exp["Day time"].unique())
print(exp["Sample source"].unique())

pivot = pd.pivot_table(exp, values="Insulin value", index="Person", columns=["Day time", "Sample source"], aggfunc="mean")
#pivot.index = pivot.index.astype(int)
#pivot = pivot.sort_index()
print(pivot)


'''
Exercise 6.2 (4 points)
Compute the mean value and standard deviation from all six columns from the previous exercise and store them in four
lists: mean_skin, std_skin, mean_plasma, and std_plasma. Print all four lists in the console for control.
Hint: you can access column data from multi-column indexes with the double index operators:
my_var = df[“index1”][“index2”]

'''
skin = pivot.xs("Skin", level="Sample source", axis=1)
plasma = pivot.xs("Plasma", level="Sample source", axis=1)

mean_skin, std_skin = skin.mean(), skin.std()
mean_plasma, std_plasma = plasma.mean(), plasma.std()

print(f"Skin mean & std {mean_skin, std_skin}, Plasma mean & std {mean_plasma, std_plasma}")


'''
Exercise 6.3 (3 points)
Based on the four lists, create a bar plot with three sections (for the three day times) and two error bars in each section
(for the two sample sources). Add a legend to the bar plot and label the x axis properly. Your plot should look like this:
'''

day_times = pivot.columns.get_level_values("Day time").unique()


x, w = np.arange(len(day_times)), 0.4
plt.bar(x, mean_skin, w, yerr = std_skin, color = "blue")
plt.bar(x + w, mean_plasma, w, yerr = std_plasma, color = "orange")
plt.xticks(x + w / 2, day_times)
plt.legend(["Skin", "Plasma"], fontsize=12)
plt.show()