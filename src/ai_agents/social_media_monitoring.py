import pandas as pd
import requests


class SocialMediaMonitoringAgent:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def connect_to_api(self):
        try:
            response = requests.get(self.base_url, headers={'Authorization': self.api_key})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")
            return None

    def gather_data(self, influencer_id):
        endpoint = f"{self.base_url}/engagement_data/{influencer_id}"
        try:
            response = requests.get(endpoint, headers={'Authorization': self.api_key})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error gathering data: {e}")
            return None

    def analyze_data(self, data):
        try:
            df = pd.DataFrame(data)
            engagement_summary = df.describe()
            return engagement_summary
        except Exception as e:
            print(f"Error analyzing data: {e}")
            return None
