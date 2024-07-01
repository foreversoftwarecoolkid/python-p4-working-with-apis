import requests
from urllib.parse import urlparse, parse_qs

class GetPrograms:
    def __init__(self, base_url="http://data.cityofnewyork.us/resource/"):
        self.base_url = base_url

    def get_programs(self, page=1):
        url = f"{self.base_url}uvks-tn5n.json?page={page}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_programs(self):
        all_programs = []
        while True:
            programs = self.get_programs()
            all_programs.extend(programs)
            # Check for a 'next' link in the Link header
            link_header = response.headers.get('Link')
            if not link_header or 'rel="next"' not in link_header:
                break
            # Extract the URL for the next page and increment the page counter
            next_page_url = next((url for url in link_header.split(',') if 'rel="next"' in url), None)
            if next_page_url:
                next_page_url = next_page_url.strip('<> ')
                page_num = int(parse_qs(urlparse(next_page_url).query)['page'][0]) + 1
                yield from self.get_all_programs(page=page_num)
