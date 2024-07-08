# main.py

import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error

def visualize_data(dataframes):
    """
    Ask user for graph preferences and create visualizations.

    Parameters:
    - dataframes (list of DataFrame): List of loaded DataFrames.
    """
    for i, df in enumerate(dataframes):
        print(f"Columns in DataFrame {i + 1}: {df.columns.tolist()}")
        plot_type = input("Enter the type of plot (e.g., line, bar, scatter): ")
        x_col = input("Enter the column name for the X-axis: ")
        y_col = input("Enter the column name for the Y-axis: ")
        
        if plot_type == 'line':
            df.plot(kind='line', x=x_col, y=y_col)
        elif plot_type == 'bar':
            df.plot(kind='bar', x=x_col, y=y_col)
        elif plot_type == 'scatter':
            df.plot(kind='scatter', x=x_col, y=y_col)
        else:
            print(f"Unsupported plot type: {plot_type}")
            continue
        
        plt.title(f"DataFrame {i + 1} {plot_type.capitalize()} Plot")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

def choose_model(df):
    """
    Ask user for the type of target column and apply appropriate models.

    Parameters:
    - df (DataFrame): DataFrame containing the dataset.
    """
    target_col = input("Enter the target column name: ")
    model_type = input("Is the target column for classification or regression? ")

    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if model_type.lower() == 'classification':
        model = LogisticRegression(max_iter=1000)
    elif model_type.lower() == 'regression':
        model = LinearRegression()
    else:
        print(f"Unsupported model type: {model_type}")
        return

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if model_type.lower() == 'classification':
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy}")
    elif model_type.lower() == 'regression':
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    dataframes = load_data()
    visualize_data(dataframes)

    # Example to choose model for the first DataFrame loaded
    if dataframes:
        choose_model(dataframes[0])
