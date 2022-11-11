import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingRegressor

X = pd.read_csv("./Tables/Ratios_sin_atipicos_LOF_3.csv",index_col = 0)
X = X.drop(['Cash Ratio'], axis=1)
Y_labeled = pd.read_csv("./Tables/Porcentajes_Y_etiquetas.csv",index_col = 0)
Y = pd.DataFrame(Y_labeled['Perf'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

"""# Stacking

"""#V4"""


model_HGB = HistGradientBoostingRegressor(learning_rate = 0.5, max_depth = 5, max_iter = 100)
model_GBR = GradientBoostingRegressor(learning_rate = 0.25, max_depth = 5, n_estimators = 100)
model_KNNR = KNeighborsRegressor(n_neighbors = 15, weights = 'uniform', leaf_size = 20)

Modelos = {('KNNR', model_KNNR), ('Gradient boosting', model_GBR)}


SCR = StackingRegressor(Modelos, final_estimator = model_HGB, cv = 5, n_jobs = 1)

SCR.fit(X_train, Y_train)

Y_pred_SCR = SCR.predict(X_test)

joblib.dump(SCR, 'model.pkl')