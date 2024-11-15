from abc import ABC, abstractmethod
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
import joblib

# Define the interface for all models
class DigitClassificationInterface(ABC):
    @abstractmethod
    def predict(self, image: np.ndarray) -> int:
        pass

# Implement CNN model class
class CNNModel(DigitClassificationInterface):
    def __init__(self):
        # Load pre-trained model (this is just an example)
        self.model = tf.keras.models.load_model('cnn_model.h5')  # Assuming the model is saved in 'cnn_model.h5'
    
    def predict(self, image: np.ndarray) -> int:
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = np.expand_dims(image, axis=-1)  # Add channel dimension (28x28x1)
        prediction = self.model.predict(image)  # Predict class probabilities
        return np.argmax(prediction)  # Return the class with the highest probability

# Implement Random Forest model class
class RandomForestModel(DigitClassificationInterface):
    def __init__(self):
        # Load pre-trained Random Forest model (example with joblib)
        self.model = joblib.load('random_forest_model.pkl')  # Assuming the model is saved in 'random_forest_model.pkl'
    
    def predict(self, image: np.ndarray) -> int:
        image = image.flatten().reshape(1, -1)  # Flatten the 28x28 image to a 1D array
        return self.model.predict(image)[0]  # Return the predicted label

# Implement Random model class
class RandomModel(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Random prediction between 0-9
        return np.random.randint(0, 10)

# Main class to select the model
class DigitClassifier:
    def __init__(self, algorithm: str):
        if algorithm == "cnn":
            self.model = CNNModel()
        elif algorithm == "rf":
            self.model = RandomForestModel()
        elif algorithm == "rand":
            self.model = RandomModel()
        else:
            raise ValueError("Invalid algorithm. Choose 'cnn', 'rf', or 'rand'.")

    def predict(self, image: np.ndarray) -> int:
        return self.model.predict(image)

# Example usage
if __name__ == "__main__":
    # Test with a random 28x28x1 image (grayscale)
    image = np.random.rand(28, 28)  # Placeholder for an actual image
    classifier = DigitClassifier('cnn')  # Choose 'cnn', 'rf', or 'rand'
    prediction = classifier.predict(image)
    print(f"Predicted digit: {prediction}")
