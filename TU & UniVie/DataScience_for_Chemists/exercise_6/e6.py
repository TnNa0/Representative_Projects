
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


#prepare data
df = pd.read_excel('./Exercise 3_data.xlsx')
df_labels = df['Unnamed: 0'] #save labels for labeling dendogram later
df_num_labels = df.drop(columns = 'Unnamed: 0') #drop object column

df_num = df_num_labels.apply(pd.to_numeric, errors='coerce')#make numeric. problem was to read in object-first row

df_clean = df_num.dropna() #removes the entire row. makes completely comparable dataset
df_labels = df_labels.loc[df_clean.index] #get same indexing


'''
Part 1: Decision Trees

(i) Consider the attribute Cost for Class labeling. Specify two classes: Expensive
and Cheap. Play with at least two thresholds for specifying the classes (e.g.,
Threshold 1=0.8 US$ means that all fuels with a cost higher than this value are in
the Class Expensive and those lower than this value would be in the Cheap). Use your
own Thresholds!

(ii) Create Decision trees using at least two different criteria (i.e., Gini, and at
least one of Entropy and Log Loss), to build the whole tree (i.e., no pruning).
You can use the rest of the default settings of the proposed python functions
or change them but always keep the ccp_alpha=0.0 parameter!). Report the
full tree structure (if possible, draw it!)

(iii) Prune the trees following the cost-complexity approach for a 10-fold cross
validation procedure. Report the best alpha value and the best pruned tree (if
possible, draw it).

(iv) Calculate the confusion matrix metrics for the selected pruned tree.

'''
#i)

#print(df_clean)
df_clean["Expensive1"] = (df_clean["Cost"] > 0.5) #set expensive threshold to 0.5
df_clean["Expensive2"] = (df_clean["Cost"] > 0.7) #set expensive threshold to 0.7
#print(df_clean)

#ii)
#gini & log_loss
#use GridSearchCV to find the best model based on param_grid (includes both criterions gini & log_loss)
#GridSearch'CV'->cross validation included
clf = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)

param_grid = {
    'criterion': ['gini', 'log_loss'],
    'max_depth': [None, 3, 5, 10],
}

grid1 = GridSearchCV(clf, param_grid, cv=10)
grid2 = GridSearchCV(clf, param_grid, cv=10)


X1 = df_clean.drop(columns=["Expensive1", "Cost"]) #remove Cost column for training, to train on more biological relevant data. Cost is too good ;)
y1 = df_clean["Expensive1"]

X2 = df_clean.drop(columns=["Expensive2", "Cost"])
y2 = df_clean["Expensive2"]

print(y1.value_counts())
print(y2.value_counts())

#reserve 10% of data for validatio metrics later. use the rest to train the model
X_train1, X_test1, y_train1, y_test1 = train_test_split(
    X1, y1, test_size=0.10, random_state=42, stratify=y1  # stratify helps preserve class balance
)

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X2, y2, test_size=0.10, random_state=42, stratify=y2  # stratify helps preserve class balance
)


# make loop to:-------todo
#.save both thresholds in variables X & y -> list? and access from list for fitting
#.save best_ into dict for 1:[] & 2:[]

grid1.fit(X_train1, y_train1)

best_params1 = grid1.best_params_
best_score1 = grid1.best_score_
best_model1 = grid1.best_estimator_

grid2.fit(X_train2, y_train2)

best_params2 = grid2.best_params_
best_score2 = grid2.best_score_
best_model2 = grid2.best_estimator_

print("depth of the best model", best_model1.tree_.max_depth)
print("node count of the best model", best_model1.tree_.node_count)


#validation of tested models with "unseen data"

y_pred1 = grid1.best_estimator_.predict(X_test1)
accuracy1 = accuracy_score(y_test1, y_pred1)
print("Final test accuracy:", accuracy1)

print(confusion_matrix(y_test1, y_pred1))
print(classification_report(y_test1, y_pred1))


y_pred2 = grid2.best_estimator_.predict(X_test2)
accuracy2 = accuracy_score(y_test2, y_pred2)
print("Final test accuracy:", accuracy2)

print(confusion_matrix(y_test2, y_pred2))
print(classification_report(y_test2, y_pred2))

#print expensive1/2 side by side

results_df1 = pd.DataFrame(grid1.cv_results_)
results_df1.sort_values(by='mean_test_score', ascending=False)
#print(results_df1)
print("Gini results:\n", results_df1[results_df1['param_criterion'] == 'gini'], 
      "\n\nLog Loss results:\n", results_df1[results_df1['param_criterion'] == 'log_loss'])


#print decision trees
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 6))

plot_tree(best_model1, 
          feature_names=X1.columns, 
          class_names=["Cheap", "Expensive"], 
          filled=True,
          fontsize=6,
          ax=axes[0])
axes[0].set_title("Decision Tree for Expensive1 (0.5)")

plot_tree(best_model2, 
          feature_names=X2.columns, 
          class_names=["Cheap", "Expensive"], 
          filled=True,
          fontsize=6,
          ax=axes[1])
axes[1].set_title("Decision Tree for Expensive2(0.7)")

plt.tight_layout()
plt.show()

#alternative plotting of decision trees in terminal
from sklearn.tree import export_text
print(export_text(best_model1, feature_names=list(X1.columns)))
print(export_text(best_model2, feature_names=list(X2.columns)))

'''
when the threshold for cost is set at 0.5 the gini criterion emered as the most effective model.
The root would be split using TE condition <= 0.53 and a second time using GWP > 2.41. This logic achieves
pure nodes for expensive & cheap.
|--- TE <= 0.53
|   |--- GWP <= 2.41
|   |   |--- class: False
|   |--- GWP >  2.41
|   |   |--- class: True
|--- TE >  0.53
|   |--- class: True

However, when the threshold is set at Cost = 0.7 the log_loss criterion was the best model.
Here, the tree depth = 3 and node_number = 6. The root is split using TE <= 0.705, then using TE <= 0.735 from expensive and
finally LO <= 0.19 ti achieve pure nodes.
|--- TE <= 0.70
|   |--- class: False
|--- TE >  0.70
|   |--- TE <= 0.74
|   |   |--- LO <= 0.19
|   |   |   |--- class: True
|   |   |--- LO >  0.19
|   |   |   |--- class: False
|   |--- TE >  0.74
|   |   |--- class: True

'''

#(iii) Prune the trees following the cost-complexity approach for a 10-fold cross
#validation procedure. Report the best alpha value and the best pruned tree (if
#possible, draw it).

# .cost_complexity_pruning_path() computes the effective alphas and the corresponding total leaf impurities 
# for pruning a tree. These alpha values represent different levels of pruning strength:
# - Lower alpha: less pruning (deeper tree)
# - Higher alpha: more pruning (shallower tree)clf.fit(X_train1, y_train1)

path = clf.cost_complexity_pruning_path(X_train1, y_train1)
ccp_alphas = path.ccp_alphas
print("pruned alpha values", ccp_alphas)

alpha_results = []

for alpha in ccp_alphas:
    tree = DecisionTreeClassifier(ccp_alpha=alpha)
    score = cross_val_score(tree, X_train1, y_train1, cv=10)
    alpha_results.append((alpha, score.mean()))

best_alpha, best_score = max(alpha_results, key=lambda x: x[1])
print("Best alpha:", best_alpha, "with mean CV score:", best_score)
'''
Best alpha: 0.0 with mean CV score: 0.9857142857142858
->no pruning is the best result! original model already good.

'''

#Part 2: Regression Trees
#(i) Consider again the Cost as the Regression Output and create the
#corresponding regression trees using at least two different criteria (i.e.,
#“squared error”, and at least one of “friedman_mse” and “absolute_error”),
#to build the whole tree. You can use the rest of the default settings of the
#proposed python functions or change them but always keep the
#ccp_alpha=0.0 parameter!). Report the full tree structure (if possible, draw
#it!)


print("\n\nPart 2:\n\n")

df_clean = df_clean.drop(columns=['Expensive1', 'Expensive2'])
X_reg = df_clean.drop(columns=["Cost"])
y_reg = df_clean["Cost"]

print(y_reg.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_reg, test_size=0.10, random_state=42
)

tree_reg = DecisionTreeRegressor()

params_grid_reg ={
    'criterion': ['squared_error', 'friedman_mse', 'absolute_error'],
    'max_depth': [None, 3, 5, 10],
}

grid_reg = GridSearchCV(tree_reg, params_grid_reg, cv=10)

grid_reg.fit(X_train, y_train)

y_pred_reg = grid_reg.best_estimator_.predict(X_test)

mse = mean_squared_error(y_test, y_pred_reg)
mae = mean_absolute_error(y_test, y_pred_reg)
r2 = r2_score(y_test, y_pred_reg)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R^2 Score:", r2)

print(export_text(grid_reg.best_estimator_, feature_names=list(X_reg.columns)))

criteria = ['squared_error', 'friedman_mse', 'absolute_error']
models = []

for crit in criteria:
    model = DecisionTreeRegressor(criterion=crit, max_depth=grid_reg.best_params_['max_depth'])
    model.fit(X_train, y_train)
    models.append(model)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
titles = ['MSE', 'Friedman MSE', 'MAE']

for i, model in enumerate(models):
    plot_tree(model, feature_names=X_reg.columns, filled=True, fontsize=6, ax=axes[i])
    axes[i].set_title(f"Criterion: {titles[i]}")

plt.tight_layout()
plt.show()

print("Model parameters:", model.get_params())

print("Depth of MSE model:", models[0].tree_.max_depth)
print("Node count:", models[0].tree_.node_count)
print("Feature importances:", models[0].feature_importances_)

importances = models[0].feature_importances_
important_features = [(name, importance) for name, importance in zip(X_reg.columns, importances)]

# Sort by importance descending
important_features.sort(key=lambda x: x[1], reverse=True)

# Print nicely
for name, importance in important_features:
    print(f"{name}: {importance:.4f}")

'''
#Strucutre Report of one tree (MSE):
Depth of MSE model: 9
Node count: 87
The most important labels for splitting was TE by far, followed by Distance, FWEU, LO, PMPF.
Water, POFP and TA did not contribute to splitting.

'''
#ii)
#(ii) Prune the trees following the cost-complexity approach for a 10-fold cross
#validation procedure. Report the best alpha value and the best pruned tree (if
#possible, draw it).

tree_reg.fit(X_train, y_train)

cost = tree_reg.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas

print("Best alpha scores", ccp_alphas)

alpha_reslt = []

for alpha in ccp_alphas:
    tree = DecisionTreeRegressor(ccp_alpha=alpha)
    score = cross_val_score(tree, X_train, y_train, cv=10)
    alpha_reslt.append((alpha, score.mean()))
best_alpha, best_score = max(alpha_reslt, key=lambda x:x[1])
print("Best alpha:", best_alpha, "with mean CV score:", best_score)

best_tree = DecisionTreeRegressor(ccp_alpha=best_alpha)
best_tree.fit(X_train, y_train)
y_pred = best_tree.predict(X_test)

# Evaluate with regression metrics
print("Test MSE:", mean_squared_error(y_test, y_pred))
print("Test R2:", r2_score(y_test, y_pred))

'''
Best alpha: 0.0 with mean CV score: 0.9857142857142858
->no pruning is the best result! original model already good.
-> very low MSE & high R2.. model seems to explain the given dataset very accurately
'''

