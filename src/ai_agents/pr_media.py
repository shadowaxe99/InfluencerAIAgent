import requests
from bs4 import BeautifulSoup
from technology_stack.backend.database.mongodb import UserProfileSchema, PressReleaseSchema

class PRMediaAgent:
    """
    Manages the generation of press releases and monitoring of media mentions for brand collaborations.
    """
    def __init__(self):
        """
        Initializes a new instance of the PRMediaAgent class.
        """
        self.userProfile = UserProfileSchema()
        self.pressReleases = PressReleaseSchema()

    def generate_press_release(self, collaboration):
        """
        Creates a press release for a brand collaboration, announcing the partnership to the public
        and media outlets. This method is used to generate buzz and inform the audience about the
        influencer's latest projects.

        Parameters:
            collaboration (dict): The brand collaboration data used to craft the press release.


        :param collaboration: The brand collaboration details.
        :return: A dictionary representing the press release.
        """
        title = f"{self.userProfile.name} collaborates with {collaboration.brand}"
        body = f"We are excited to announce a new collaboration between {self.userProfile.name} and {collaboration.brand}. Stay tuned for more updates!"
        press_release = {
            "title": title,
            "body": body,
            "date": collaboration.date
        }
        self.pressReleases.insert_one(press_release)
        return press_release

    def monitor_media(self, keyword):
        """
        Monitors media outlets for mentions of specific keywords related to the influencer or brand collaborations.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines containing the keyword.
        """
        """
        Monitors various media outlets for mentions of the influencer or specific keywords related to their brand and activities. This function helps in tracking the influencer's media presence and public perception.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors media outlets for mentions of the influencer or related keywords, helping to track the influencer's media presence and public perception.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of the influencer or topics related to their brand collaborations and interests. This method helps in tracking the influencer's media presence and public perception.

        Parameters:
            keyword (str): The keyword or phrase to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors media outlets for mentions of the influencer or related topics, providing insights into public perception and media coverage.

        Parameters:
            keyword (str): The keyword or phrase to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of the influencer or specific keywords related to their brand or niche. This helps in tracking the influencer's media presence and public perception.

        Parameters:
            keyword (str): The keyword to monitor in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of specific keywords related to the influencer or brand.
        This method helps in tracking the media presence and public perception of the influencer's brand collaborations.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of specific keywords related to the influencer or brand. This method helps in tracking the media presence and public perception of the influencer's brand collaborations.

        Parameters:
            keyword (str): The keyword to monitor in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of the influencer or specific keywords related to their brand or niche.
        This method helps in tracking the influencer's media presence and public perception.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword was mentioned.
        """
        """
        Monitors media outlets for mentions of the influencer or related keywords. This method helps influencers stay informed
        about their public perception and the reach of their brand collaborations.

        Parameters:
            keyword (str): The keyword to search for in media outlets.

        Returns:
            list: A list of headlines or articles where the influencer or keyword is mentioned.
        """
        """
        Monitors various media outlets for mentions of specific keywords related to the influencer or brand.
        This function is useful for tracking the reach and impact of press releases and other media content.

        Parameters:
            keyword (str): The keyword to monitor in media outlets.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Searches for media mentions of a specific keyword, which can be the influencer's name, brand name, or any
        relevant term. This method helps in tracking the media presence and public perception of the influencer or brand.

        Parameters:
            keyword (str): The keyword to search for in media articles.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Searches for media mentions of a specific keyword, which can be the influencer's name, brand name, or any
        relevant term. This method helps in tracking the media presence and public perception of the influencer or brand.

        Parameters:
            keyword (str): The keyword to search for in media articles.

        Returns:
            list: A list of headlines or articles where the keyword is mentioned.
        """
        """
        Searches for media mentions of a given keyword, such as the influencer's name or a brand they are collaborating with.
        This method uses web scraping to gather headlines from news sources, providing insights into media coverage.

        Parameters:
            keyword (str): The keyword to search for in media mentions.

        Returns:
            list: A list of headlines that include the given keyword.
        """
        """
        Monitors media mentions by searching for a given keyword.
        :param keyword: The keyword to search for in media articles.
        :return: A list of media headlines that mention the keyword.
        """
        url = f"https://news.google.com/news?q={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('a', {'class': 'DY5T1d'})
        return [headline.text for headline in headlines]
