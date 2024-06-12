from colors import colors
from web_scrapper import bfs_search
from bs4 import BeautifulSoup
import re, requests, sys, warnings

warnings.filterwarnings("ignore", message="Unverified HTTPS request.*")

def find_titles(start_url: str, target_pattern: str) -> list[tuple[str, str]]:
	print(f"{colors.GREEN}Waiting scraper to do its job...{colors.END}")
	found_urls = bfs_search(start_url, target_pattern, 2)
	print(f"{colors.GREEN}Done! Finding titles...{colors.END}")
	titles: list[tuple[str, str]] = []

	for url in found_urls:
		response = requests.get(url, verify=False)
		if response.status_code == 200:
			soup = BeautifulSoup(response.content, 'html.parser')
			links = soup.find_all('a')
			for link in links:
				text = link.get_text(strip=True)
				decoded_text = text.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding).replace('\r\n', ' ')
				titles.append((decoded_text, (re.sub(r"(.*\/)Makalah.*\.htm", r"\1", url) + link.get("href", '/')).replace(' ', "%20")))
		else:
			print("Failed to retrieve the webpage. Status code:", response.status_code)
	return titles
