
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq


#from sklearn.metrics import r2_score

#exercise 7.1

print("exercise 7.1")

data_lin = pd.read_excel("/home/anton/Lectures/MultiOmics/ex07/Sheet_07/Regression-points.xlsx")
data_nlin = pd.read_excel("/home/anton/Lectures/MultiOmics/ex07/Sheet_07/Regression-points.xlsx", sheet_name = "Nonlinear")

#print(data_lin.describe(),"\n", data_lin.info(),"\n", data_lin.head())
#print(data_nlin.describe(),"\n", data_nlin.info(),"\n", data_nlin.head())

x_lin_mean, y_lin_mean = data_lin["X"].mean(), data_lin["Y"].mean()

m = sum(data_lin["X"] * (data_lin["Y"] - y_lin_mean)) / sum(data_lin["X"] * (data_lin["X"] - x_lin_mean))
b = y_lin_mean - m * x_lin_mean

print("m & b:", m, b)


xmod = np.arange(min(data_lin["X"]), max(data_lin["X"]), 0.001)
ymod = m * xmod + b

plt.scatter(data_lin["X"], data_lin["Y"], label = "Linear Dataset")
plt.plot(xmod, ymod, color = "red", label = "Modell")
plt.legend()
plt.show()

y_pred_lin = m * data_lin["X"] + b

ss_res_lin = np.sum((data_lin["Y"] - y_pred_lin) ** 2)
ss_tot_lin = np.sum((data_lin["Y"] - data_lin["Y"].mean()) ** 2)

r2_lin = 1 - (ss_res_lin / ss_tot_lin)

print("Linear R2:", r2_lin)


def michaelis_menten_model(Vmax, Km, X):
    return (Vmax * X) / (Km + X)


def michaelis_menten_res_func(par, X, Y):
    Vmax, Km = par
    predicted_Y = michaelis_menten_model(Vmax, Km, X)
    return Y - predicted_Y


X = data_nlin["X"]
Y = data_nlin["Y"]

start_par = [1, 1]

result = leastsq(
    michaelis_menten_res_func,
    start_par,
    args=(X, Y)
)

Vmax_opt, Km_opt = result[0]

xment = np.arange(min(X), max(X), 0.001)
yment = michaelis_menten_model(Vmax_opt, Km_opt, xment)

plt.scatter(X, Y, label="Non-Linear Dataset")
plt.plot(xment, yment, color="red", label="Model")
plt.legend()
plt.show()

print("Vmax:", Vmax_opt)
print("Km:", Km_opt)

y_pred_nlin = michaelis_menten_model(Vmax_opt, Km_opt, X)

ss_res_nlin = np.sum((Y - y_pred_nlin) ** 2)
ss_tot_nlin = np.sum((Y - Y.mean()) ** 2)

r2_nlin = 1 - (ss_res_nlin / ss_tot_nlin)

print("Michaelis-Menten R2:", r2_nlin)




#exercise 7.3

print("exercise 7.3")

x_extrap_lin = 10
y_extrap_lin = m * x_extrap_lin + b

print("Curve 1 at x = 10:", y_extrap_lin)


x_extrap_nlin = 130
y_extrap_nlin = michaelis_menten_model(Vmax_opt, Km_opt, x_extrap_nlin)

print("Curve 2 at x = 130:", y_extrap_nlin)
