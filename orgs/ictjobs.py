import requests
from bs4 import BeautifulSoup


def scrape():
	# Only getting 50 most pertinent job offers
	url = "https://www.ictjob.be/fr/rss?function=168,761,685,165,162,160&devskills=&sysskills=&busskills=&studyLevels=&experiences=&keywords=&keywords_options=OR&contractTypes=&jobModes=&contractDurations=&regions=&sectors=&searchLanguage=1,2&departments=&locationItems=&numResult=202"
	page = requests.get(url)
	
	# Getting jobs
	soup = BeautifulSoup(page.content, "html.parser")
	jobs_elt = soup.find_all("title")[1:]
	new_jobs = []
	for job in jobs_elt:
		new_jobs.append(job.text.lower())

	return new_jobs