import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from xgboost import XGBRegressor

class Models_trainer:
        def __init__(self) -> None:
                self.df = pd.read_csv('data/encoded_data.csv')
                self.df.drop('Unnamed: 0',axis=1,inplace=True)
                self.df = self.df.dropna()
                self.X = self.df.drop('price',axis=1,inplace=False)
                self.y = self.df['price']
                self.X_train = None
                self.X_test = None
                self.y_train = None
                self.y_test = None
        
        def split_data_Set(self):
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,random_state=124)
        
        def train_linearregression(self):
            print('LinearRegression')
            regressor = LinearRegression()
            regressor.fit(self.X_train,self.y_train)
            regressor.score(self.X_train,self.y_train)
            test_prediction = regressor.predict(self.X_test)
            regressor.score(self.X_test,self.y_test)
            print(f'train score : {regressor.score(self.X_train,self.y_train)}')
            print(f'score : {regressor.score(self.X_test,self.y_test)}')
            print(f'MAE : {mean_absolute_error(self.y_test,test_prediction)}')
            print(f'RMSE : {root_mean_squared_error(self.y_test,test_prediction)}')

        def train_xgb(self):
            print('XGBoost')
            regressor = XGBRegressor(n_estimators=1800, subsample=0.8, min_child_weight=3, max_depth=8, learning_rate=0.1, gamma=0.2, colsample_bytree=0.20,reg_alpha=0.1,reg_lambda=1)
            regressor.fit(self.X_train, self.y_train, )
            regressor.score(self.X_train,self.y_train)
            test_prediction =regressor.predict(self.X_test)
            y_train_pred = regressor.predict(self.X_train)
            y_test_pred = test_prediction
            print(f'train score : {regressor.score(self.X_train,self.y_train)}')
            print(f'score : {regressor.score(self.X_test,self.y_test)}')
            print(f'MAE : {mean_absolute_error(self.y_test,test_prediction)}')
            print(f'RMSE : {root_mean_squared_error(self.y_test,test_prediction)}')