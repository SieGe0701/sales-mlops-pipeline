import pandas as pd
import numpy as np
import mlflow
import mlflow.xgboost
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os

mlflow.set_tracking_uri("http://localhost:5000")


# -------- 1. Prepare Data --------
def load_data():
    # Load Walmart sales dataset
    data_path = "D:\college\Projects\MLops\sales-mlops-pipeline\data\Walmart_Sales.csv"
    # data_path = os.path.join("data", "sales_data.csv")
    df = pd.read_csv(data_path)

    # Parse Date column correctly with dayfirst=True
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    # Select Features
    features = [
        'Store',
        'Holiday_Flag',
        'Temperature',
        'Fuel_Price',
        'CPI',
        'Unemployment'
    ]
    
    target = 'Weekly_Sales'

    X = df[features]
    y = df[target]

    return X, y

# -------- 2. Train Model --------
def train_model(X_train, y_train, params):
    model = xgb.XGBRegressor(**params)
    model.fit(X_train, y_train)
    return model

# -------- 3. Evaluate Model --------
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    return mse, mae, r2

# -------- 4. Main Training Function --------
def main():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    mlflow.set_experiment("Walmart_Sales_Prediction_XGBoost")

    # Define model hyperparameters
    params = {
        "n_estimators": 100,
        "max_depth": 5,
        "learning_rate": 0.1,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "random_state": 42
    }

    with mlflow.start_run():
        model = train_model(X_train, y_train, params)
        mse, mae, r2 = evaluate_model(model, X_test, y_test)

        # Log all hyperparameters
        for param_name, param_value in params.items():
            mlflow.log_param(param_name, param_value)

        # Log metrics
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # Log model artifact
        mlflow.xgboost.log_model(model, artifact_path="sales_model")

        print(f"XGBoost model trained and logged successfully!")
        print(f"MSE: {mse:.2f}, MAE: {mae:.2f}, R2: {r2:.2f}")

if __name__ == "__main__":
    main()
