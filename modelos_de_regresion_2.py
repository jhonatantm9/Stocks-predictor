import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import joblib

X_LOF = pd.read_csv("./Tables/Ratios_sin_atipicos_LOF.csv", index_col = 0)
X_LOF = X_LOF.drop(['Cash Ratio'], axis=1)
X_LOF.reset_index(inplace=True, drop=True)

Y_LOF = pd.read_csv("./Tables/Porcentajes_Y_LOF.csv", index_col = 0)
Y_LOF.reset_index(inplace=True, drop=True)


"""Train test split"""
X_train, X_test, Y_train, Y_test = train_test_split(X_LOF, Y_LOF['Perf'], test_size=0.2, random_state=0)

"""# Histogram gradient boosting"""
model_HGB = HistGradientBoostingRegressor(learning_rate = 0.05, max_depth = 5, max_iter = 100).fit(X_train, Y_train)

"""# Gradient boosting regressor"""
model_GBR = GradientBoostingRegressor(learning_rate = 0.06, max_depth = 5, n_estimators = 100).fit(X_train, Y_train)

"""# Random forest regression"""
model_RFR = RandomForestRegressor(max_depth=5, n_estimators=100).fit(X_train, Y_train)

""" Random Forest Regressor Polynomic"""
pf = PolynomialFeatures(degree = 3)    # usaremos polinomios de grado 3
X_train_pol = pf.fit_transform(X_train)
X_test_pol = pf.fit_transform(X_test)
modelo_rfr_pol = RandomForestRegressor(max_depth=5, n_estimators=100)


"""# Stacking"""
Modelos = {('Histogram boosting', model_HGB), ('Gradient boosting', model_GBR),
           ('Random Forest', model_RFR), ('Modelo RFR Polinomico', modelo_rfr_pol)}

LR = LinearRegression()
SCR = StackingRegressor(Modelos, final_estimator = LR, cv = 2, n_jobs = 1)
SCR.fit(X_train, Y_train)
Y_pred = SCR.predict(X_test)

joblib.dump(SCR, 'model.pkl')