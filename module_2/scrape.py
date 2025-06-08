import urllib3
from urllib3.exceptions import HTTPError
from urllib import robotparser
from bs4 import BeautifulSoup

class GradCafeScraper:
    """
    A web scraper for extracting data from TheGradCafe's survey pages.

    Attributes:
        base_url (str):   The root URL of the website to scrape.
        path (str):       The path on the website to the survey data.
        user_agent (str): Identifier used for checking access permissions in robots.txt.
        http (urllib3.PoolManager): HTTP connection manager for sending requests.
    """

    def __init__(self, base_url='https://www.thegradcafe.com', path='/survey', user_agent='natali'):
        """
        Initializes the GradCafeScraper with optional base URL, path, and user-agent.
  
        Args:
            base_url (str):   Base URL of the target website.
            path (str):       Path to the specific survey page.
            user_agent (str): User agent string for robots.txt compliance.
        """

        self.base_url   = base_url
        self.path       = path
        self.user_agent = user_agent
        self.http       = urllib3.PoolManager()

    def _check_permissions(self):
        """
        Checks if the scraper has permission to access the target page
        by reading and parsing the site's robots.txt file.

        Raises:
            ConnectionError: If the request to robots.txt fails.
            PermissionError: If the user-agent is not allowed to access the specified path.
        """

        url = self.base_url + '/robots.txt'

        try:
            # Fetch and decode the robots.txt file from the website
            response = self.http.request('GET', url)
            txt      = response.data.decode('utf-8')

        except HTTPError as e:
            # Raise an error if connection fails
            raise ConnectionError(f"Failed to connect to {url}: {e}")
        
        # Parse robots.txt to check permissions
        parser = robotparser.RobotFileParser()
        parser.parse(txt.splitlines())
        
        # Verify that the user-agent is allowed to access the target path
        allowed = parser.can_fetch(self.user_agent, self.base_url + self.path)
        if not parser.can_fetch(self.user_agent, self.base_url + self.path):
            raise PermissionError(f"Access to '{self.base_url + self.path}' is disallowed for user-agent '{self.user_agent}'.")

    def scrape_data(self, page_num):
        """
        Scrapes data from TheGradCafe survey pages up to the specified page number.

        Args:
            page_num (int): The number of pages to scrape (starts from page 1 up to page_num - 1).

        Returns:
            list: A list of BeautifulSoup 'tr' (table row) elements containing the scraped data.
        
        Raises:
            PermissionError: If access to the target page is disallowed by robots.txt.
            ConnectionError: If any page fails to load.
        """

        self._check_permissions()

        rows = []

        # Iterate through the specified number of pages
        for num in range(1, page_num):
            url = self.base_url + self.path + '/index.php?q=&page=' + str(num)

            # Request and decode the HTML content of the page
            response = self.http.request('GET', url)
            html     = response.data.decode('utf-8')

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")

            # Collect all table rows - Each entry_num has 2 table rows that contain information.
            rows.extend(soup.find_all('tr'))

        return rows