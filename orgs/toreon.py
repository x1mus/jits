import requests
from bs4 import BeautifulSoup

def scrape():
	# Getting the page
	url = "https://jobpage.cvwarehouse.com/?companyGuid=611d716e-9a0c-4414-8355-da02597f86b4&lang=en-US"
	page = requests.get(url)

	# Getting jobs
	soup = BeautifulSoup(page.text, "html.parser")
	jobs_elt = soup.find_all("div", class_="mosaic-item")
	new_jobs = []
	for job in jobs_elt:
		new_jobs.append(job.find("div", class_="job-title").text.lower())

	return new_jobs