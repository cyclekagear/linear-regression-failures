import numpy as np

def generate_linear_data(n_samples=100, noise_std=1.0):
    """
    Generates linear data: y = 3x + 5 + noise
    """
   
    x = np.random.uniform(-5, 5, n_samples)
    noise = np.random.normal(0, noise_std, n_samples)
    y = 3 * x + 5 + noise
    x = x.reshape(-1, 1)
    return x, y


def generate_quadratic_data(n_samples=100, noise_std=1.0):
    """
    Generates quadratic data: y = 3x^2 + 5x + 2 + noise
    """
    x = np.random.uniform(-5, 5, n_samples)
    noise = np.random.normal(0, noise_std, n_samples)
    y = x**2+ noise
    x = x.reshape(-1, 1)
    return x, y