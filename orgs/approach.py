import requests
from bs4 import BeautifulSoup

def scrape():
	# Getting the page
	url = "https://www.approach.be/en/jobs.html"
	page = requests.get(url)


	# Getting jobs
	soup = BeautifulSoup(page.text, "html.parser")
	jobs_elt = soup.find_all("div", class_="job-list-simple")
	new_jobs = []
	for job in jobs_elt:
		new_jobs.append(job.find("h2").text.lower())

	return new_jobs