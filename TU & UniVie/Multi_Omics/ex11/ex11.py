import pandas as pd
import numpy as np

print("ex11.1")

data = pd.read_csv("/home/anton/Lectures/MultiOmics/ex11/Sheet_11/cardio.csv", sep=";")
#print(data.head())
feat = data.loc[:, data.columns != "State"].columns.to_list()

x = data.loc[:, data.columns != "State"]
X = pd.DataFrame()
#normalization of x to X
for feature in feat:
    X.loc[:, feature] = (x[feature] - x[feature].mean()) / x[feature].std()

X.to_numpy()
y = data["State"].to_numpy()

print("ex11.2")
#"run each classifier and report accuracy in for loop"

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.model_selection import cross_validate



models = {
"tree": tree.DecisionTreeClassifier(random_state = 0),
"randomforest": RandomForestClassifier(random_state = 0),
"ann": MLPClassifier(random_state = 0),
"bayes": GaussianNB(),
"svm" : svm.SVC(kernel = "linear", random_state = 0)}

acc = {}

for name, model in models.items():
    cv_result = cross_validate(model, X, y, cv = 5, scoring = "accuracy")
    acc[name] = cv_result["test_score"].mean()

print(acc)
print(max(acc, key=acc.get))


print("ex11.3")

rf  = models["ann"]
rf.fit(X, y)


train_mean = x.mean(axis=0)
train_std = x.std(axis=0)

unknown = pd.DataFrame(
    [[6.7, 0.61, 0.08, 2.1, 0.089, 12, 44, 0.99, 3.47, 0.55, 10.1, 6]],
    columns=feat)

unknown_norm = (unknown - train_mean) / train_std

result = rf.predict(unknown_norm)
print(result)


print("ex11.4")
from random import shuffle

svm = models["svm"]
shuffle(y)

cv_result = cross_validate(svm, X, y, cv = 10, scoring = "accuracy")
result = cv_result["test_score"].mean()

print(result)
