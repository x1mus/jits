import json, re
from bs4 import BeautifulSoup
from selenium import webdriver


def createHeadlessFirefoxBrowser():
	options = webdriver.FirefoxOptions()
	options.add_argument("--headless")
	return webdriver.Firefox(options=options)

def scrape():
	# Setting up the page
	browser = createHeadlessFirefoxBrowser()
	browser.get("https://nato.taleo.net/careersection/2/jobsearch.ftl")
	browser.find_element_by_xpath("//select[@name='dropListSize']/option[text()='100']").click()

	# Getting jobs
	soup = BeautifulSoup(browser.page_source, "html.parser")
	table = soup.find(id="requisitionListInterface.listRequisition")
	jobs_elt = table.find_all("span", class_="titlelink")
	new_jobs = []
	for job in jobs_elt:
		new_jobs.append(job.find("a").text.lower())

	with open("jobs.json", "r") as f:
		saved_jobs = json.loads(f.read())

	# Checking if "nato" exists in the json file
	if "nato" not in saved_jobs.keys():
		saved_jobs["nato"] = []

	# Removing out of date jobs
	out_jobs = []
	for job in saved_jobs["nato"]:
		if job not in new_jobs:
			old_jobs.append(job)
	for job in out_jobs:
		saved_jobs["nato"].remove(job)

	# Adding new jobs at the beginning
	to_add = []
	for job in new_jobs:
		if job not in saved_jobs["nato"]:
			to_add.append(job)
	for job in to_add:
		saved_jobs["nato"].append(job)

	# Saving new jobs
	with open("jobs.json", "w") as f:
		f.write(json.dumps(saved_jobs))