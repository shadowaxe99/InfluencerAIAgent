
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class AnalystAgent:
    """
    AnalystAgent is responsible for performing data analysis to aid in strategic decision-making.

    It handles preprocessing of input data, training a predictive model (RandomForestRegressor),
    making predictions with the trained model, and evaluating its performance. It is specifically
    tailored for analyzing strategy-related insights inferred from the given data.

    Attributes:
        data (pd.DataFrame): The input data, converted into a pandas DataFrame upon initialization.
        model (RandomForestRegressor, optional): The trained predictive model, initialized as None.
        X_train (pd.DataFrame, optional): Training feature set, initialized as None.
        X_test (pd.DataFrame, optional): Testing/validation feature set, initialized as None.
        y_train (pd.Series, optional): Training target values, initialized as None.
        y_test (pd.Series, optional): Testing/validation target values, initialized as None.
    """

    def __init__(self, data):
        # Initialize the agent with the provided data and set all other attributes to None.
        self.data = pd.DataFrame(data)  # Convert the input data to a pandas DataFrame.
        self.model = None               # Placeholder for the predictive model to be trained later.
        self.X_train = None             # Placeholder for the training feature set.
        self.X_test = None              # Placeholder for the testing/validation feature set.
        self.y_train = None             # Placeholder for the training target values.
        self.y_test = None              # Placeholder for the testing/validation target values.

    def preprocess_data(self, target_column='strategyInsights'):
        # Preprocess the input data in preparation for model training.
        self.data.dropna(inplace=True)  # Remove any rows with missing values.
        self.data = pd.get_dummies(self.data)  # Convert categorical variables into dummy/indicator variables.
        X = self.data.drop(target_column, axis=1)  # Extract features by dropping the target column.
        y = self.data[target_column]  # Extract the target column as the labels.
        # Split the data into training and testing sets with a 80-20 split.
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    def train_model(self, model=None, params=None):
        # Train the predictive model using the preprocessed training data.
        if model is None:
            model = RandomForestRegressor
        if params is None:
            params = {'n_estimators': 100, 'random_state': 42}
        self.model = model(**params)
        self.model.fit(self.X_train, self.y_train)
    
    def predict(self, input_data):
        # Use the trained model to make predictions on new, unseen data.
        return self.model.predict(input_data)  # Returns the predicted values.

    def evaluate_model(self):
        # Evaluate the performance of the trained model using the testing set.
        predictions = self.model.predict(self.X_test)  # Make predictions on the testing set.
        # Calculate and return the Mean Absolute Error (MAE) between the predictions and the true labels.
        return metrics.mean_absolute_error(self.y_test, predictions)

    def analyze_strategy(self, input_data, target_column='strategyInsights'):
        # Run the full analysis pipeline on the provided input data, targeting a specific column for insights.
        self.preprocess_data(target_column=target_column)  # Preprocess the data with the specified target column.
        self.train_model()  # Train the model with the preprocessed data.
        prediction = self.predict(input_data)  # Make a prediction based on the input data.
        performance = self.evaluate_model()  # Evaluate the model's performance.
        return prediction, performance  # Return both the prediction and the performance metric.

