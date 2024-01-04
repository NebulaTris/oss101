from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import StratifiedShuffleSplit

import pandas as pd

housing_data=fetch_california_housing()
data=housing_data.data

X=pd.DataFrame(housing_data.data,columns=housing_data.feature_names)
y=pd.DataFrame(housing_data.target,columns=housing_data.target_names)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=49)

lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)

target_predictions=lin_reg.predict(X_test)
print("Mean Squared Error:",mean_squared_error(y_test,target_predictions))