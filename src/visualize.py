import matplotlib.pyplot as plt
import numpy as np

def plot_data_with_line(x, y, y_pred, title=""):
    """
    Plots a scatter plot of data points and a regression line.
    
    Parameters:
    x (array-like): Feature values (e.g., shape 100x1)
    y (array-like): Actual target values
    y_pred (array-like): Predicted values from the model
    title (str): Title of the plot
    """
    # Ensure inputs are numpy arrays and flattened to 1D
    x = np.array(x).ravel()
    y = np.array(y).ravel()
    y_pred = np.array(y_pred).ravel()
    
    # 0. Sort x and y_pred based on x values
    # This is necessary for plt.plot to draw a continuous line instead of a mess
    sort_idx = np.argsort(x)
    x_sorted = x[sort_idx]
    y_pred_sorted = y_pred[sort_idx]
    
    # 1. scatter(x, y) - original data points
    plt.scatter(x, y, color='blue', alpha=0.6, label='Actual Data')
    
    # 2. plot(x, y_pred) - the model prediction line
    plt.plot(x_sorted, y_pred_sorted, color='red', linewidth=2, label='Model Line')
    
    # 3. labels + title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    
    # Show or save the plot
    plt.show()
