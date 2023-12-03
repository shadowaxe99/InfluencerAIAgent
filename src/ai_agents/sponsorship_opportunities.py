import pandas as pd
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SponsorshipOpportunitiesAgent:
    def __init__(self, interests, niche, demographics):
        self.interests = interests
        self.niche = niche
        self.demographics = demographics
        self.opportunities = pd.DataFrame()

    def scan_opportunities(self, sources):
        for source in sources:
            response = requests.get(source)
            soup = BeautifulSoup(response.text, 'html.parser')
            sponsorships = soup.find_all('a', {'class': 'sponsorship'})
            for sponsorship in sponsorships:
                self.opportunities = self.opportunities.append({'sponsorship': sponsorship.text}, ignore_index=True)

    def match_opportunities(self):
        self.opportunities['match'] = self.opportunities['sponsorship'].apply(lambda x: any(i in x for i in self.interests))

    def recommend_opportunities(self):
        vectorizer = CountVectorizer().fit_transform(self.opportunities['sponsorship'])
        vectors = vectorizer.toarray()
        csim = cosine_similarity(vectors)
        self.opportunities['score'] = csim.sum(axis=1)

    def report_opportunities(self):
        return self.opportunities.sort_values(by=['score'], ascending=False)
