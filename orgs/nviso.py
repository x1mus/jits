import json, re
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

	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	# Checking if "nviso" exists in the json file
	if "nviso" not in saved_jobs.keys():
		saved_jobs["nviso"] = []

	# Removing out of date jobs
	out_jobs = []
	for job in saved_jobs["nviso"]:
		if job not in new_jobs:
			old_jobs.append(job)
	for job in out_jobs:
		saved_jobs["nviso"].remove(job)

	# Adding new jobs at the beginning
	to_add = []
	for job in new_jobs:
		if job not in saved_jobs["nviso"]:
			to_add.append(job)
	for job in to_add:
		saved_jobs["nviso"].append(job)

	# Saving new jobs
	with open("jobs.json", "w") as f:
		f.write(json.dumps(saved_jobs))