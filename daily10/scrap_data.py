#Scrapping hackernews for top 10 news of the day//

from bs4 import BeautifulSoup
import requests


def string_slicer(string: str) -> int:
    """custom string slicer"""
    if string != 'None':
        required_string = int(string.split('>')[1].split(' ')[0])
        return required_string
    else:
        return 0


class ScrapData:

    def __init__(self, site_url):
        response = requests.get(url=site_url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def get_data(self):
        """returns a dictionary of news APIs"""
        stories = []
        for item in self.soup.select('.athing'):
            title = item.select_one('.titleline').a.text
            link = item.select_one('.titleline').a['href']
            subtext = item.find_next_sibling('tr').select_one('.subtext')
            score = subtext.select_one('.score')
            score = str(score)
            stories.append(
                {
                    "title": title,
                    "link": link,
                    "score": string_slicer(score),
                }
            )

        return stories


if __name__ == '__main__':
    scraped_data = ScrapData('https://news.ycombinator.com/')
    news_data = scraped_data.get_data()
    for news in news_data:
        print(news)
