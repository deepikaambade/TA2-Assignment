# model.py

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_linear_regression_model(X_train, y_train):
    """
    Train a linear regression model.

    Parameters:
    - X_train (DataFrame): Features matrix for training.
    - y_train (Series): Target variable for training.

    Returns:
    - model (LinearRegression): Trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Define other modeling functions...

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model.

    Parameters:
    - model: Trained model object.
    - X_test (DataFrame): Features matrix for testing.
    - y_test (Series): Target variable for testing.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Mean Squared Error:", mse)
    print("R^2 Score:", r2)
