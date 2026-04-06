import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data/scoring.csv")
x = data.drop(columns=["default"]).values
y = data["default"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LogisticRegression(class_weight="balanced")
model.fit(x_train, y_train)

joblib.dump(model, "model.pkl")