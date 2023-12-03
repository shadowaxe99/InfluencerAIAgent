import requests


class BrandManager:
    def __init__(self, user_profile, brand_collaboration_data):
        self.user_profile = user_profile
        self.brand_collaboration_data = brand_collaboration_data

    def find_partnership_opportunities(self):
        opportunities = []
        for brand in self.brand_collaboration_data:
            if brand['compatibility_score'] > 80 and brand['collaboration_status'] == 'potential':
                opportunities.append(brand)
        return opportunities

    def analyze_collaboration_performance(self):
        performance_metrics = {}
        for brand in self.brand_collaboration_data:
            if brand['collaboration_status'] == 'active':
                performance_metrics[brand['name']] = {
                    'engagement_rate': brand['engagement_rate'],
                    'conversion_rate': brand['conversion_rate'],
                    'roi': brand['roi']
                }
        return performance_metrics
