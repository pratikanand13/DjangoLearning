from sklearn.datasets import load_iris  
data = load_iris()  
import pandas as pd
X_data = pd.DataFrame(data.data , columns = data.feature_names)
y_data = pd.Series(data = data.target, name = 'Targets')

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_data,y_data,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

from joblib import dump

# Your data
data_to_save = accuracy_score(y_test,y_pred)  # Replace with the data you want to save

# Specify the filename where you want to save the data
filename = './savedModels/model.joblib'

# Save the data to the specified filename
dump(accuracy_score(y_test,y_pred), filename)
