# -*- coding: utf-8 -*-
"""Heart_disease_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/175wVbl9cbQHLr_EUD3i_ZJWYMlUdtg5T
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

###
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('/content/framingham_heart_diseas.csv')
data.describe

data.isna().sum()

data.dropna(axis = 0, inplace = True)
print(data.shape)

x = data.iloc[:,0:15]
y = data.iloc[:,15:16]

x.head()

y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

score = logreg.score(X_test, y_test)
print("Prediction score is:",score)

from sklearn.metrics import confusion_matrix, classification_report 
cm = confusion_matrix(y_test, y_pred) 
print("Confusion Matrix is:\n",cm)

print("Classification Report is:\n\n",classification_report(y_test,y_pred))
