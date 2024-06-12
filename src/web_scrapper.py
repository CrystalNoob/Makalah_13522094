from bs4 import BeautifulSoup
from urllib.parse import urljoin
from queue import Queue
import re, requests, warnings

warnings.filterwarnings("ignore", message="Unverified HTTPS request.*")

def bfs_search(start_url: str, target_pattern: str, max_depth: int) -> set[str]:
	queue: Queue[tuple[str, int]] = Queue()
	queue.put((start_url, 0))
	visited_urls: set[str] = set()
	target_regex = re.compile(target_pattern, re.IGNORECASE)
	found_urls: set[str] = set()
	depth: int = 0

	while not queue.empty() and depth < max_depth:
		url, depth = queue.get()
		if url in visited_urls:
			continue
		visited_urls.add(url)

		try:
			if url.endswith((".htm", ".html")):
				response = requests.get(url, verify=False)
				if response.status_code == 200:
					soup = BeautifulSoup(response.text, 'html.parser')
					links = soup.find_all('a', href=True)
					for link in links:
						absolute_url = urljoin(url, link['href'])
						if target_regex.search(absolute_url):
							found_urls.add(absolute_url)
						queue.put((absolute_url, depth + 1))

		except requests.exceptions.RequestException as e:
			print("Error occurred while processing URL:", url)
			break

	if len(found_urls) == 0:
		print("No target URLs found")
		return found_urls
	else:
		return found_urls
