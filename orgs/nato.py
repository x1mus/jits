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

	return new_jobs