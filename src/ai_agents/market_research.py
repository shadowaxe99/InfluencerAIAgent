import pandas as pd
import requests
from bs4 import BeautifulSoup


class MarketResearchAgent:
    def __init__(self, api_keys, competitors):
        self.api_keys = api_keys
        self.competitors = competitors

    def get_market_trends(self, niche):
        url = f'https://api.market-trends.com/{niche}'
        response = requests.get(url, headers=self.api_keys)
        return response.json()

    def get_competitor_analysis(self, competitor):
        url = f'https://www.competitor-analysis.com/{competitor}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('div', {'class': 'data'})

    def get_demographics(self, audience):
        url = f'https://api.demographics.com/{audience}'
        response = requests.get(url, headers=self.api_keys)
        return response.json()

    def process_data(self, market_trends, competitor_analysis, demographics):
        df = pd.DataFrame(market_trends)
        df['competitor_data'] = [data.text for data in competitor_analysis]
        df['demographics'] = demographics
        return df

    def generate_report(self, df):
        report = df.describe()
        return report

def get_market_research_report(api_keys, niche, competitors, audience):
    agent = MarketResearchAgent(api_keys, competitors)
    market_trends = agent.get_market_trends(niche)
    competitor_analysis = [agent.get_competitor_analysis(competitor) for competitor in competitors]
    demographics = agent.get_demographics(audience)
    df = agent.process_data(market_trends, competitor_analysis, demographics)
    report = agent.generate_report(df)
    return report
