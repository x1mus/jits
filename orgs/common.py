import json, re
from . import approach, ictjobs, nato, nviso, toreon

sites = ["approach", "ictjobs", "nato", "nviso", "toreon"]

def scrape(site_name):
	if site_name in sites:
		new_jobs = eval(site_name + ".scrape()")
	else:
		print("Unrecognized website")
		exit()

	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	# Checking if the site name exists in the json file
	if site_name not in saved_jobs.keys():
		saved_jobs[site_name] = []

	# Removing out of date jobs
	out_jobs = []
	for job in saved_jobs[site_name]:
		if job not in new_jobs:
			out_jobs.append(job)
	for job in out_jobs:
		saved_jobs[site_name].remove(job)

	# Adding new jobs at the beginning
	to_add = []
	for job in new_jobs:
		if job not in saved_jobs[site_name]:
			to_add.append(job)
	for job in to_add:
		saved_jobs[site_name].append(job)

	# Saving new jobs
	with open("jobs.json", "w") as f:
		f.write(json.dumps(saved_jobs))

def display(site_name, keyword=None):
	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	if site_name not in saved_jobs.keys(): return

	i = 0
	for job in saved_jobs[site_name]:
		if keyword:
			if re.search(keyword, job):
				print(f"{site_name} - {i:03} - {job}")
				i += 1
		else:
			print(f"{site_name} - {i:03} - {job}")
			i += 1