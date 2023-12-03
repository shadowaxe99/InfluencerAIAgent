import pandas as pd
import requests


class AudienceEngagementAgent:
    def __init__(self, api_keys):
        self.api_keys = api_keys

    def get_data(self, platform, user_id):
        if platform == 'facebook':
            url = f'https://graph.facebook.com/{user_id}/insights'
            params = {'access_token': self.api_keys['facebook']}
        elif platform == 'twitter':
            url = f'https://api.twitter.com/1.1/users/show.json?user_id={user_id}'
            params = {'Authorization': 'Bearer ' + self.api_keys['twitter']}
        response = requests.get(url, params=params)
        return response.json()

    def analyze_data(self, data):
        df = pd.DataFrame(data)
        insights = {
            'average_likes': df['likes'].mean(),
            'average_comments': df['comments'].mean(),
            'average_shares': df['shares'].mean()
        }
        return insights

    def report_insights(self, insights):
        report = f"Average Likes: {insights['average_likes']}\n" \
                 f"Average Comments: {insights['average_comments']}\n" \
                 f"Average Shares: {insights['average_shares']}"
        return report

def get_audience_engagement_report(api_keys, platform, user_id):
    agent = AudienceEngagementAgent(api_keys)
    data = agent.get_data(platform, user_id)
    insights = agent.analyze_data(data)
    report = agent.report_insights(insights)
    return report
