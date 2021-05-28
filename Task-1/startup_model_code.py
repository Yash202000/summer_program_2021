import pandas as pd
import numpy as np

# READING CSV FILE
dataset = pd.read_csv('50_Startups.csv')

# LABEL ENCODING
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
final_state = encoder.fit_transform(dataset['State']).reshape(-1,1)
Y=dataset['Profit'].values.reshape(-1,1)
X = dataset[['R&D Spend', 'Administration','Marketing Spend']].values

# PERFORMING ONEHOTENCODING
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
final = ohe.fit_transform(final_state)
final= final.toarray()
final_state = final[:,0:2]
X=np.hstack((X,final_state))

# TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.33, random_state=42)

# TRAINING MODEL
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

# SAVING MODEL INTO satartupmodel.pk1
import joblib
joblib.dump(model,'startupmodel.pk1')
