"""
Script for making predictions on test data using the trained polynomial regression model.
The model and transformer are loaded from the saved files.
"""

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pickle
import argparse

def predict(data_path):
    # Load the trained model and transformer
    try:
        with open('polynomial_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        with open('polynomial_transformer.pkl', 'rb') as transformer_file:
            poly = pickle.load(transformer_file)
        
        # Load the test data
        data = pd.read_csv(data_path)
        
        # Ensure the test data contains the correct feature
        if '6' not in data.columns:
            raise KeyError("The test data must contain the '6' feature.")
        
        # Prepare the data for prediction
        feature = data['6'].values.reshape(-1, 1)
        feature_poly = poly.transform(feature)
        
        # Make predictions
        predictions = model.predict(feature_poly)
        
        # Save predictions to a CSV file
        data['predictions'] = predictions
        data.to_csv('predictions.csv', index=False)
        
        print(f"Predictions saved to 'predictions.csv'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make predictions on test data using the trained model.")
    parser.add_argument("data_path", type=str, help="Path to the test data CSV file.")
    args = parser.parse_args()
    
    predict(args.data_path)
