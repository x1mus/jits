import json, re
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

	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	# Checking if "ictjobs" exists in the json file
	if "ictjobs" not in saved_jobs.keys():
		saved_jobs["ictjobs"] = []

	# Removing out of date jobs
	out_jobs = []
	for job in saved_jobs["ictjobs"]:
		if job not in new_jobs:
			old_jobs.append(job)
	for job in out_jobs:
		saved_jobs["ictjobs"].remove(job)

	# Adding new jobs at the beginning
	to_add = []
	for job in new_jobs:
		if job not in saved_jobs["ictjobs"]:
			to_add.append(job)
	for job in to_add:
		saved_jobs["ictjobs"].append(job)

	# Saving new jobs
	with open("jobs.json", "w") as f:
		f.write(json.dumps(saved_jobs))

def display(keyword=None):
	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	if "ictjobs" not in saved_jobs.keys(): return

	i = 0
	for job in saved_jobs["ictjobs"]:
		if keyword:
			if re.search(keyword, job):
				print(f"ictjobs - {i:03} - {job}")
				i += 1
		else:
			print(f"ictjobs - {i:03} - {job}")
			i += 1