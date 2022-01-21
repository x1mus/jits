import json, re
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

	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	# Checking if "approach" exists in the json file
	if "approach" not in saved_jobs.keys():
		saved_jobs["approach"] = []

	# Removing out of date jobs
	out_jobs = []
	for job in saved_jobs["approach"]:
		if job not in new_jobs:
			old_jobs.append(job)
	for job in out_jobs:
		saved_jobs["approach"].remove(job)

	# Adding new jobs at the beginning
	to_add = []
	for job in new_jobs:
		if job not in saved_jobs["approach"]:
			to_add.append(job)
	for job in to_add:
		saved_jobs["approach"].append(job)

	# Saving new jobs
	with open("jobs.json", "w") as f:
		f.write(json.dumps(saved_jobs))

def display(keyword=None):
	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	if "approach" not in saved_jobs.keys(): return

	i = 0
	for job in saved_jobs["approach"]:
		if keyword:
			if re.search(keyword, job):
				print(f"approach - {i:03} - {job}")
				i += 1
		else:
			print(f"approach - {i:03} - {job}")
			i += 1