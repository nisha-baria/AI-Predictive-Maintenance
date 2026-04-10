import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# dataset load
data = pd.read_csv("data/iot_sensor_data.csv")

# features
X = data[['temperature','vibration','current']]
y = data['failure']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "models/model.pkl")

print("MODEL TRAINED SUCCESSFULLY")