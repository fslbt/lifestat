import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

data_root = "https://raw.githubusercontent.com/ageron/data/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")

X = lifesat[["GDP per capita (USD)"]].values
y = lifesat["Life satisfaction"].values

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "lifesat_model.pkl")

print("Model trained and saved")