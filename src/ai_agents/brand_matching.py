import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


class BrandMatchingAgent:
    def __init__(self):
        self.influencer_data = None
        self.brand_data = None

    def gather_data(self, influencer_data_path, brand_data_path):
        self.influencer_data = pd.read_csv(influencer_data_path)
        self.brand_data = pd.read_csv(brand_data_path)

    def match_influencer(self, n_clusters):
        data = pd.concat([self.influencer_data, self.brand_data])
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
        return kmeans.labels_

    def evaluate_match(self, labels):
        score = silhouette_score(self.influencer_data, labels)
        return score
