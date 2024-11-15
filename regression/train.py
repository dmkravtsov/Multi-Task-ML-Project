"""
Script for training a polynomial regression model on Feature 6 and the target variable.
Saves the trained model and evaluation metrics.
"""

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import pickle
import argparse

def main(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Extract the feature and target
    X = data['6'].values.reshape(-1, 1)  # Feature 6
    y = data['target'].values  # Target variable
    
    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    
    # Train the polynomial regression model
    model = LinearRegression()
    model.fit(X_poly, y)
    
    # Evaluate the model
    r2 = r2_score(y, model.predict(X_poly))
    rmse = np.sqrt(mean_squared_error(y, model.predict(X_poly)))
    
    # Save the model and the polynomial transformer
    with open('polynomial_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    
    with open('polynomial_transformer.pkl', 'wb') as transformer_file:
        pickle.dump(poly, transformer_file)
    
    # Print metrics
    print(f"Model trained successfully!")
    print(f"R² score: {r2}")
    print(f"RMSE: {rmse}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a polynomial regression model.")
    parser.add_argument("data_path", type=str, help="Path to the dataset CSV file.")
    args = parser.parse_args()
    
    main(args.data_path)
