import requests
from bs4 import BeautifulSoup

def scrape():
	# Getting the page
	url = "https://www.nviso.eu/en/jobs"
	page = requests.get(url)

	# Getting jobs
	soup = BeautifulSoup(page.text, "html.parser")
	jobs_elt = soup.find_all("div", class_="vacancy-item")
	new_jobs = []
	for job in jobs_elt:
		new_jobs.append(job.find("span").text.lower())

	return new_jobs