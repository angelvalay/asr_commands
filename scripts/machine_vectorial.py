import pandas as pd
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#load data
from sklearn.svm import SVC
data_features = pd.read_csv('../data/features_voice.csv', thousands=' ')
# Dropping unneccesary columns
data_features = data_features.drop(['filename'],axis=1)
command_list = data_features.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(command_list)
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data_features.iloc[:, :-1], dtype = float))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

svm = SVC(kernel='poly', random_state=1, gamma=50.0, C=1.0)
svm.fit(X_train_std, y_train)

from sklearn.metrics import accuracy_score
y_pred=svm.predict(X_test_std)
print(accuracy_score(y_test, y_pred))


from sklearn.externals import joblib
joblib.dump(svm, "../models/my_model.pkl") # save
my_model_loaded = joblib.load("../models/my_model.pkl") # load
