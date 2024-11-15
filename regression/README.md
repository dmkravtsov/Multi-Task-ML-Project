## Project Overview

- Analyze the dataset and its structure.
- Conduct exploratory data analysis (EDA).
- Identify key patterns and dependencies between features and the target variable.
- Model the target variable to uncover predictive relationships.
- Draw conclusions based on the modeling results.

## Data Description

- The dataset contains **53 features** and **1 target variable**.
- Features include **43 continuous variables** (`float64`) and **11 integer variables** (`int64`).
- The dataset has **no missing values** or **duplicates**.
- The target variable (`target`) is continuous, ranging from **0 to 100**, with a mean of **50.03** and moderate variability (`std ≈ 28.90`).

## Feature Selection

- **Recursive Feature Elimination (RFE)** with cross-validation was used to reduce the feature space.
- RFE identified **Feature 6** and **Feature 7** as the most relevant predictors.

## Key Insights from Visual Analysis

- **Feature 6**:
  - Displays a clear **polynomial relationship** with the target variable based on the scatterplot.
- **Feature 7**:
  - Shows no discernible pattern or dependency with the target variable.

## Polynomial Regression Results

- After confirming the significance of **Feature 6**, a polynomial regression (degree 2) was applied:
  - **Quadratic term coefficient**: **1.0000**
  - **Linear term coefficient**: **-0.00008** (negligible impact)
  - **Intercept**: **0.4975**
  - **R² score**: **0.9999**, indicating an almost perfect fit.
  - **Root Mean Squared Error (RMSE)**: **0.2887**, confirming excellent prediction accuracy.

## Conclusions

1. **Feature 6** exhibits a strong quadratic relationship with the target variable, making it a crucial predictor.
2. **Feature 7** does not contribute meaningfully and can be disregarded.
3. Polynomial regression effectively models the relationship between **Feature 6** and the target, providing high predictive accuracy as reflected in both **R²** and **RMSE** metrics.

## Next Steps

- Validate the polynomial regression model on unseen data.
- Explore other potential non-linear models to compare performance.
- Investigate feature engineering opportunities for enhancing predictive power.

## How to Use the Training Script

To train the polynomial regression model, use the provided `train.py` script. The script expects a dataset in the form of a CSV file. Ensure your data file is named `train.csv` and contains the necessary columns: **'6'** for the feature and **'target'** for the target variable.

### Running the Script

Open your terminal and execute the following command:


python train.py train.csv

## How to Use the `predict.py` Script

The `predict.py` script is designed for making predictions on test data using the trained polynomial regression model. The model and transformer are loaded from previously saved files, and predictions are made on the feature `6`.

### Prerequisites

1. Ensure the following files are in the same directory:
   - `polynomial_model.pkl` — The trained polynomial regression model.
   - `polynomial_transformer.pkl` — The polynomial feature transformer.
   
2. The test data file **must contain the column '6'** (the feature used for prediction).

### Running the Script

1. Open the terminal.
2. Run the following command:


python predict.py hidden_test.csv


## How to Install Dependencies

To install the necessary dependencies for this project, you can use the provided `requirements.txt` file. 

### Steps:

1. Ensure you have **pip** installed (Python's package installer).
2. Run the following command in your terminal:


pip install -r requirements.txt

