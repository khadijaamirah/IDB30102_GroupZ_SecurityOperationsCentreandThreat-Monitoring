import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load CIC-IDS2017 dataset
dataset_path = "CIC-IDS2017.csv"
data = pd.read_csv(dataset_path)

print("Dataset loaded successfully.")


# Clean column names
data.columns = data.columns.str.strip()


# Remove invalid and missing values
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.dropna(inplace=True)


# Convert traffic labels into binary classes
# BENIGN = 0
# Malicious = 1
data["Binary_Label"] = data["Label"].apply(
    lambda x: 0 if str(x).strip().upper() == "BENIGN" else 1
)


# Select numerical features
X = data.select_dtypes(include=[np.number]).copy()

if "Binary_Label" in X.columns:
    X = X.drop(columns=["Binary_Label"])

y = data["Binary_Label"]


# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Proposed model: Random Forest
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

random_forest.fit(X_train, y_train)
rf_predictions = random_forest.predict(X_test)


# Baseline model: Decision Tree
decision_tree = DecisionTreeClassifier(
    random_state=42,
    class_weight="balanced"
)

decision_tree.fit(X_train, y_train)
dt_predictions = decision_tree.predict(X_test)


# Function to evaluate each model
def evaluate_model(model_name, actual, predicted):

    accuracy = accuracy_score(actual, predicted)
    precision = precision_score(actual, predicted, zero_division=0)
    recall = recall_score(actual, predicted, zero_division=0)
    f1 = f1_score(actual, predicted, zero_division=0)

    print(f"\n{model_name}")
    print("------------------------------")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")


# Evaluate and compare the models
evaluate_model(
    "Random Forest",
    y_test,
    rf_predictions
)

evaluate_model(
    "Decision Tree",
    y_test,
    dt_predictions
)
