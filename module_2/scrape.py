import urllib3
from urllib3.exceptions import HTTPError
from urllib import robotparser
from bs4 import BeautifulSoup

class GradCafeScraper:
    def __init__(self, base_url='https://www.thegradcafe.com', path='/survey', user_agent='natali'):
        self.base_url   = base_url
        self.path       = path
        self.user_agent = user_agent
        self.http       = urllib3.PoolManager()

    def _check_permissions(self):
        url = self.base_url + '/robots.txt'

        try:
            response = self.http.request('GET', url)
            txt      = response.data.decode('utf-8')

        except HTTPError as e:
            raise ConnectionError(f"Failed to connect to {url}: {e}")
        
        parser = robotparser.RobotFileParser()
        parser.parse(txt.splitlines())

        allowed = parser.can_fetch(self.user_agent, self.base_url + self.path)
        if not parser.can_fetch(self.user_agent, self.base_url + self.path):
            raise PermissionError(f"Access to '{self.base_url + self.path}' is disallowed for user-agent '{self.user_agent}'.")

    def scrape_data(self, page_num):
        self._check_permissions()

        rows = []

        # Loop through pages
        for num in range(1, page_num):
            url = self.base_url + self.path + '/index.php?q=&page=' + str(num)

            # Request data from URL
            response = self.http.request('GET', url)
            html     = response.data.decode('utf-8')

            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")

            # Collect all table rows - Each entry_num has 2 table rows that contain information.
            rows.extend(soup.find_all('tr'))

        return rows