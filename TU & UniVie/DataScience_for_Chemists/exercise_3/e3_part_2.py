
"""
Formulate and Solve the Linear Programming (LP) Dual Problem (slide 35,
including the constraint for λ values). This means the problem should be
formulated and solved 72 times by changing the objective function every time
(i.e., target unit). Tabulate the results (efficiency scores, λ values, and the values
of slack variables) clearly denoting the efficient routes.

For two inefficient routes of your choice identify the peer group of efficient
routes and the corresponding target values for the inefficient units to become
efficient. --> projection
"""
import numpy as np
import pandas as pd
from pulp import *

df = pd.read_excel('./Exercise 3_data.xlsx')

df_labels = df.iloc[:, 0] #store labels for later = DMU
df_labels = df_labels.drop(index=df_labels.index[0]).dropna()

df_clean = df.drop(df.columns[0], axis=1).drop(index=df.index[0]).dropna() #removes the entire row. makes completely comparable dataset

df_num = df_clean.apply(pd.to_numeric, errors='coerce')#make numeric. problem was to read in object-first row

df_norm = ((df_num - df_num.min()) / (df_num.max() - df_num.min())) #min max normalization

x = df_norm.shape[1] #cols
y = df_norm.shape[0] #rows

#collect results from objective function
list_z = []
lam_matrix= []
slack_matrix = []

#Declare each constraint based on observed value, lambda and slack ... use list comprehension []
"""
For each row we need one constraint (double=Transposed), which contains each column * the respective lambda
"""
for dmu in range(y):

    current_lam_row = []
    current_slack_row = []
    #LP Inizilized
    prob = LpProblem('DEA_BioFuels', LpMinimize)

    #Descision Varibale Declared
    lam=LpVariable.dict('lambda', range(y), lowBound=0, cat='Continuous')
    slack=LpVariable.dict('slack', range(x), lowBound=0, cat='Continuous')
    z=LpVariable('eff', lowBound=0, cat='Continuous')

    #Declare Objective Function
    prob += z

    #Loop to collect all lambdas and slack for each dmu //basically here the linear problem i ssolved for each element!
    for n_col in range(x):
            prob += lpSum([lam[n_row] * df_norm.iloc[n_row, n_col] for n_row in range(y)]) + slack[n_col] == z * df_norm.iloc[dmu, n_col]

    #Convexity constraint
    prob += lpSum([lam[n_row] for n_row in range(y)]) == 1

    #print(prob)
    
    #Solve Problem
    status=prob.solve()
    #print(LpStatus[status])

    current_lam_row = [lam[n_row].varValue for n_row in range(y)]
    current_slack_row = [slack[n_col].varValue for n_col in range(x)]
    lam_matrix.append(current_lam_row)
    slack_matrix.append(current_slack_row)
    

    #Print Objective Value
    list_z.append(z.varValue)
    #print(z.varValue)

df_lam_matrix = pd.DataFrame(lam_matrix, 
                                columns = df_labels.values, 
                                index = df_labels.values
                                )

df_slack_matrix = pd.DataFrame(slack_matrix, 
                                columns = df_clean.columns, #accessing the input features, stored as headers
                                index = df_labels.values
                                )

df_results = pd.DataFrame({
        'DMU': df_labels.values,
        'Efficiency': list_z
})

print("OVERVIEW\n[--------------------------------------------------------------------------------")
print("Input Matrix:\n", df_clean.head())
print("Shape of Input Matrix:\n", df_clean.shape)

print("Z-score matrix:\n", df_results)
print("Sum of all z-scores:\n", df_results.sum())

print("Lambda Matrix:\n", df_lam_matrix)
print("Slack Matrix:\n", df_slack_matrix)
print("--------------------------------------------------------------------------------\n")

inefficient = df_results[df_results['Efficiency']<1]
print("Inefficient:\n",inefficient.sort_values('Efficiency').head(2))

#.>get peer group rom lambda matrix, and comput projection.

dmus = ['E85 corn D', 'E85 corn/stover B']

for dmu in dmus:
        lam_row = df_lam_matrix.loc[dmu]
        peers = lam_row[lam_row > 0]
        print(f"\n*Peer* Groups for {dmu} (lambda-weights):\n{peers}")
        target_value = df_norm.T @ df_lam_matrix.loc[dmu].values.reshape(-1, 1)
        print(f"\n*Projected* {dmu}:\n {target_value}")
        target_slack = df_slack_matrix.loc[dmu]
        print(f"\nTarget *Slack* Values {dmu}:\n {target_slack.sort_values(ascending=False)}")

total_slack_per_sum = df_slack_matrix.sum()
print(f"\nOverall Where to improve {dmu}:\n {total_slack_per_sum.sort_values(ascending=False)}")

#print(df_norm.T.shape)
#print(df_lam_matrix.loc[dmu].shape)



"""
-------------------------------------------------------------------------------------------------------------------------
z = 1	🔥 The DMU is efficient (on the DEA frontier). Its inputs cannot be proportionally reduced while staying feasible.
z < 1	🛠 The DMU is inefficient. You could reduce all its inputs proportionally by 1 - z while still remaining feasible.
z = 0	🚨 Not valid — usually means your model is broken or constraints don’t tie z correctly.
z ≈ 1.0xx	Very slightly inefficient — close to the frontier. Solver tolerance may also explain values just above 1.
-------------------------------------------------------------------------------------------------------------------------
Collect z per DMU → build the Efficiency column

Extract the λ-weights → to identify peer groups

Analyze slacks → to see where inefficiencies exist

Do target projection for inefficient DMUs
"""

"""

Output report:
...Two groups with least z-scores were identified. Meaning that the labels do not describe them well.

Inefficient:
                   DMU  Efficiency
36         E85 corn D    0.370603
41  E85 corn/stover B    0.426877

...The Corresponding Peergroups were Identified based on the lambda weights (only shown for one inefficient group; for other see output).

*Peer* Groups for E85 corn D (lambda-weights):
E85 corn stover*G    0.074047
E85 Miscanthus       0.231663
E85 MSW              0.694291
Name: E85 corn D, dtype: float64

...and used for projection to the front-line. !-->best to use those inefficient with strongly efficient peers!!


*Projected* E85 corn D:
                  0
Distance  0.000000
Cost      0.113065
LO        0.039379
Water     0.047686
GWP       0.218956
FWET      0.318693
FWEU      0.056385
HT        0.050289
PMPF      0.130445
POFP      0.094744
TA        0.359190
TE        0.104029

..target slack values were computed. meaning even after projection we still need to improve by the following amount in the respective DMUs

Target *Slack* Values E85 corn D:
 POFP        0.235430
HT          0.137358
GWP         0.096131
PMPF        0.092821
FWET        0.051910
FWEU        0.043860
TA          0.011413
Water       0.003262
LO          0.000000
Cost        0.000000
Distance    0.000000
TE          0.000000

...based on this proposal to improve.

Overall Where to improve E85 corn/stover B:
 POFP        7.459926
Distance    5.595431
HT          3.937232
PMPF        3.547548
GWP         2.700696
FWEU        2.213217
TE          2.084418
TA          2.026522
Cost        1.966954
FWET        1.577182
Water       0.933958
LO          0.795396

"""