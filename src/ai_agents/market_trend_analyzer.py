import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class MarketTrendAnalyzerAgent:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def process_market_data(self, target_column='marketTrends'):
        self.data.dropna(inplace=True)
        self.data = pd.get_dummies(self.data)
        X = self.data.drop(target_column, axis=1)
        y = self.data[target_column]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_trend_model(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def predict_trends(self, input_data):
        return self.model.predict(input_data)

    def evaluate_trend_model(self):
        predictions = self.model.predict(self.X_test)
        return metrics.mean_absolute_error(self.y_test, predictions)
