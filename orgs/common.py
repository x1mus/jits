import json, re


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