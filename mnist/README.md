# MNIST Classifier Project

## Overview

This project implements a **digit classification system** for recognizing handwritten digits from the MNIST dataset using three different models:
1. **Convolutional Neural Network (CNN)** — A deep learning model used for image classification.
2. **Random Forest Classifier** — A machine learning model that works with flattened image data.
3. **Random Model** — A simple model that generates a random digit prediction (0-9).

The goal of this project is to create a flexible **DigitClassifier** class that can switch between these three models and predict the digit in a given **28x28x1** image.

## Key Features

- **DigitClassificationInterface**: This is an abstract class that defines the structure for all models. Each model must implement the `predict` method that takes a **28x28x1** image and returns a predicted digit (integer).
  
- **Three Models**:
  - **CNNModel**: A Convolutional Neural Network model that uses a pre-trained CNN for digit prediction.
  - **RandomForestModel**: A Random Forest Classifier model that works with a flattened version of the image (784-dimensional vector).
  - **RandomModel**: A simple model that generates a random digit between 0 and 9.
  
- **DigitClassifier**: The main class that selects the model based on the input parameter (`'cnn'`, `'rf'`, or `'rand'`) and uses the chosen model to make predictions.

## How to Use

1. **Train the Models**:
   - The models should be pre-trained. You can use a **CNN model** using TensorFlow/Keras and a **Random Forest model** using scikit-learn. Once trained, the models are saved for later use.
   
2. **Run the Classifier**:
   - After training the models, you can use the **DigitClassifier** class to load the selected model and predict the digit from a **28x28x1** image.
   
3. **Choose the Algorithm**:
   - You can choose the model to use for classification by passing the appropriate algorithm name to the **DigitClassifier** class: `'cnn'`, `'rf'`, or `'rand'`.

## Model Details

- **CNNModel**: The CNN model uses a simple architecture with convolutional layers, pooling layers, and dense layers. The model is pre-trained and loaded from a `.h5` file.
  
- **RandomForestModel**: This model uses the **RandomForestClassifier** from **scikit-learn** and is trained on a flattened version of the image (28x28 pixels → 784 features). The trained model is loaded from a `.pkl` file.
  
- **RandomModel**: This model simply returns a random digit between 0 and 9, providing a baseline or for testing purposes.

## Conclusion

This project demonstrates how to implement a flexible digit classifier that can choose between multiple machine learning models for digit classification. The system is designed to be extensible, allowing other developers to add more models in the future. The focus is on using pre-trained models and performing accurate predictions for handwritten digits.
