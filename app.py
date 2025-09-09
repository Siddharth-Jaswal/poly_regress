import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# let's create the dataset first

df = pd.DataFrame({
    "x" : [x for x in range(-100, 101)],
    "y" : [x**2 for x in range(-100, 101)]
})


X = df[["x"]]
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

