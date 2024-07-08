# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    """
    Ask user for graph preferences and create visualizations.

    Parameters:
    - df (DataFrame): DataFrame to visualize.
    """
    print(f"Columns in DataFrame: {df.columns.tolist()}")
    plot_type = input("Enter the type of plot (e.g., line, bar, scatter): ")
    x_col = input("Enter the column name for the X-axis: ")
    y_col = input("Enter the column name for the Y-axis: ")
    color = input("Enter the color for the plot (optional, press enter to skip): ")
    font_size = input("Enter the font size for the plot (optional, press enter to skip): ")

    plt.figure(figsize=(10, 6))
    
    if plot_type == 'line':
        sns.lineplot(data=df, x=x_col, y=y_col, color=color if color else None)
    elif plot_type == 'bar':
        sns.barplot(data=df, x=x_col, y=y_col, color=color if color else None)
    elif plot_type == 'scatter':
        sns.scatterplot(data=df, x=x_col, y=y_col, color=color if color else None)
    else:
        print(f"Unsupported plot type: {plot_type}")
        return

    plt.title(f"{plot_type.capitalize()} Plot of {y_col} vs {x_col}")
    plt.xlabel(x_col, fontsize=int(font_size) if font_size else None)
    plt.ylabel(y_col, fontsize=int(font_size) if font_size else None)
    plt.show()

# Add other specific visualization functions as needed...
