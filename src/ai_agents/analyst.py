
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class AnalystAgent:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def preprocess_data(self):
        self.data.dropna(inplace=True)
        self.data = pd.get_dummies(self.data)
        X = self.data.drop('strategyInsights', axis=1)
        y = self.data['strategyInsights']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def predict(self, input_data):
        return self.model.predict(input_data)

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)
        return metrics.mean_absolute_error(self.y_test, predictions)

    def analyze_strategy(self, input_data):
        self.preprocess_data()
        self.train_model()
        predictions = self.predict(input_data)
        # Evaluate model performance using multiple metrics
        mae = metrics.mean_absolute_error(self.y_test, predictions)
        mse = metrics.mean_squared_error(self.y_test, predictions)
        r2 = metrics.r2_score(self.y_test, predictions)
        # Generate actionable insights based on predictions
        suggested_actions = []
        for prediction in predictions:
            if prediction > 0.8:
                action = 'Consider scaling this strategy up as predictions are highly positive.'
            elif prediction < 0.3:
                action = 'Reevaluate the strategy, performance is predicted to be low.'
            else:
                action = 'No major changes needed, but consider minor tweaks.'
            suggested_actions.append(action)
        # Compile performance metrics
        performance = {
            'MAE': mae,
            'MSE': mse,
            'R2': r2
        }
        # Return a tuple consisting of the predictions, performance metrics, and suggested actions
        return predictions, performance, suggested_actions