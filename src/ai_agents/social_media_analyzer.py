import requests
from bs4 import BeautifulSoup


class SocialMediaAnalyzer:
    def __init__(self, user_profile, social_media_data):
        self.user_profile = user_profile
        self.social_media_data = social_media_data

    def analyze_engagement(self):
        likes = sum(post['likes'] for post in self.social_media_data)
        shares = sum(post['shares'] for post in self.social_media_data)
        comments = sum(post['comments'] for post in self.social_media_data)
        followers = self.user_profile['followers']
        return {'likes': likes, 'shares': shares, 'comments': comments, 'followers': followers}

    def analyze_performance(self):
        engagement = self.analyze_engagement()
        posts_count = len(self.social_media_data)
        average_likes = engagement['likes'] / posts_count
        average_shares = engagement['shares'] / posts_count
        average_comments = engagement['comments'] / posts_count
        engagement_rate = (average_likes + average_shares + average_comments) / engagement['followers']
        return {'average_likes': average_likes, 'average_shares': average_shares, 'average_comments': average_comments, 'engagement_rate': engagement_rate}

    def analyze_trends(self):
        trends = []
        for i in range(1, len(self.social_media_data)):
            if self.social_media_data[i]['likes'] > self.social_media_data[i-1]['likes']:
                trends.append('Increasing likes')
            if self.social_media_data[i]['shares'] > self.social_media_data[i-1]['shares']:
                trends.append('Increasing shares')
            if self.social_media_data[i]['comments'] > self.social_media_data[i-1]['comments']:
                trends.append('Increasing comments')
        return trends
