from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

# 1. Load Iris dataset
iris = load_iris()

# 2. Create a dictionary with individual features
iris_dict = {
    "sepal_length": iris.data[:, 0],
    "sepal_width":  iris.data[:, 1],
    "petal_length": iris.data[:, 2],
    "petal_width":  iris.data[:, 3],
    "labels":       iris.target
}

# 3. Load X from individual features
X = np.column_stack([
    iris_dict["sepal_length"],
    iris_dict["sepal_width"],
    iris_dict["petal_length"],
    iris_dict["petal_width"]
])

y = iris_dict["labels"]

# 4. Train Logistic Regression Model
model = LogisticRegression(multi_class="multinomial", solver="lbfgs", max_iter=200)
model.fit(X, y)

# 5. Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully in model.pkl")
