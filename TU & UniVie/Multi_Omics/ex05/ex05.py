import pandas as pd
import numpy as np


print("exercice 5.1")

iris = pd.read_csv("iris.csv", sep=";", )
print(iris)


print("\nexercise 5.2")

"""
• How many numerical values are > 3
• How many sepal_width values are > 4
• How many numerical values with species = setosa are < 2
"""
num_only = iris.iloc[:,:4]
larger3 = (num_only > 3) .sum().sum()
sepal_width_larger_4 = (num_only["sepal_width"]>4).sum()

sorted_setosa = iris.sort_values("species")
print(sorted_setosa)

count_setosa = (sorted_setosa["species"] == "setosa").sum()
print(count_setosa)
#print(iris.iloc[:50, :])
only_setosa = iris.iloc[:50, :]
#print(only_setosa.iloc[:, :4])
species_setosa_smaller2 = (only_setosa.iloc[:,:4] < 2).sum().sum()

iris[(iris["species"] == "setosa") & (iris["species"] == "virginica")]


print(f"numerical values in the iris data set > 3: {larger3}, \n sepal width values greater 4: {sepal_width_larger_4}, \n species is setas and value < 2: {species_setosa_smaller2}" )

print("\nexercise 5.3")

"""
• Compute the sum of all sepal_width values
• Compute the arithmetic mean of all petal_width values
• Compute the standard deviation of all sepal_length values
"""

sum_sepal_width = (iris["sepal_width"]).sum()
amean_sepal_width = iris["sepal_width"].mean()
std_sepal_length = iris["sepal_length"].std()

print(f"sum of all sepal width values: {sum_sepal_width},\n arithmetic mean of all petal width values: {amean_sepal_width}, \n std of all sepal length values: {std_sepal_length}" )

print("\nexercise 5.4")

"""
Group the dataset according to the species with the average as aggregation function. Answer the following questions:
• What is the mean value of setosa / petal_width, print this single value in the console
• What is the highest sepal_length mean value of the three values?
• How many of these twelve values are < 2?
"""

grouped = iris.groupby("species").mean()
print(grouped)
s_d_p = grouped.loc["setosa", "petal_width"]
longest = grouped["sepal_length"].max()
g2 = (grouped < 2).sum().sum()
print(f" the mean value of setosa / petal_width: {s_d_p}, \n highest sepal length of all: {longest}, \n number of values smaller 2: {g2} ")