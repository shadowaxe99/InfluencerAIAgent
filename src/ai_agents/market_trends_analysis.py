import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class MarketTrendsAnalysisAgent:
    def __init__(self, market_data):
        self.market_data = pd.DataFrame(market_data)
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def ingest_data(self):
        self.market_data.dropna(inplace=True)
        self.market_data = pd.get_dummies(self.market_data)

    def preprocess_data(self, target_column='trend'):
        X = self.market_data.drop(target_column, axis=1)
        y = self.market_data[target_column]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def analyze_trends(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def report_findings(self):
        predictions = self.model.predict(self.X_test)
        return {'predictions': predictions.tolist()}

    def analyze_social_media_trends(self, social_media_data):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(social_media_data)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        return filtered_sentence
