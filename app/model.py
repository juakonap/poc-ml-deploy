import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle


def h_cms(h):
    return int(h.split('\'')[0])*30.48+\
    int(h.split('\'')[1].replace('"',''))*2.54


data = pd.read_csv('data/age_of_marriage_data.csv')
data.dropna(inplace=True)

X = data.loc[:,['gender','height','religion','caste','mother_tongue','country']]
y = data.age_of_marriage


enc = LabelEncoder()
X.loc[:,['gender','religion','caste','mother_tongue','country']]= \
X.loc[:,['gender','religion','caste','mother_tongue','country']].apply(enc.fit_transform)
X['height_cms'] = X.height.apply(h_cms)
X.drop('height',inplace=True,axis=1)


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

model = RandomForestRegressor(n_estimators=80,max_depth=11)
model.fit(X_train,y_train)
y_predict = model.predict(X_test)


print("MAE : ", mean_absolute_error(y_test,y_predict))
r2_score(y_test,y_predict)

pickle.dump(model, open('data/marriage_age_predict_model.ml', 'wb'))