# preprocessing.py

from sklearn.model_selection import train_test_split

def preprocess_data(df):
    """
    Preprocess the data by handling missing values, encoding categorical variables, etc.

    Parameters:
    - df (DataFrame): DataFrame containing the medical insurance dataset.

    Returns:
    - X (DataFrame): Features matrix after preprocessing.
    - y (Series): Target variable after preprocessing.
    """
    # Preprocessing steps...
    return X, y
def preprocess_data(df):
    """
    Preprocess the DataFrame by handling NaN values and other cleaning tasks.

    Parameters:
    - df (DataFrame): DataFrame to preprocess.

    Returns:
    - df (DataFrame): Preprocessed DataFrame.
    """
    # Example: Fill NaN values with the mean of the column
    df = df.fillna(df.mean())
    return df

if __name__ == "__main__":
    dataframes = load_data()
    dataframes = [preprocess_data(df) for df in dataframes]
    visualize_data(dataframes)

    if dataframes:
        choose_model(dataframes[0])
