# JITS - Scraping IT and Cybersecurity jobs easily

This repository aims at making it easy for students, job seekers and others to find a job in the field of IT or cybersecurity by keeping it very simple.

## Description

It has probabaly already occured to you to scroll through a lot of company websites to find and apply for jobs. The tasks is tedious, some company implement their job pages very poorly and it takes then forever to navigate through all of them !

But since you're probably like me (lazy), this tool is made for you. There's two basic features that are very easy to use, "scraping" which recovers the latests job offers from every implemented websites and "display" which (surprise, surprise, ...) displays the job offers available according to a keyword or company filter.

## Getting started
### Dependencies
This tool is written in python and uses 3 differents external libraries :
- BeautifulSoup4
- Requests
- Selenium

In order to make selenium work you'll also need to install the Firefox's *GeckoDriver*.

This tool has been tested on a Linux environment so Windows support might be off.

### Installing
To install the python3 libraries :
```bash
$ pip3 install -r requirements.txt
```

To install geckodriver :
- The releases are available on the [geckodriver github](https://github.com/mozilla/geckodriver/releases)
- Once you have the release download, you just extract it
- You can move it `mv geckodriver /usr/local/share/`
- Create a symlink `ln -sf /usr/local/share/geckodriver /usr/local/bin`

### Executing the program
Jits works in three different modes. You can launch the "scrape/display" modes without any arguments and it will execute them for every implemented sites :
```bash
$ python3 jits.py scrape # This will populate/update the "jobs.json" file
$ python3 jits.py display # This will display the "jobs.json" file
$ python3 jits.py info # This will display all implemented websites
```

If you don't want to scrape/display every possible sites, you can choose to target a specific site :
```bash
$ python3 jits.py scrape -s "nviso" # This will populate/update the "nviso" part in the "jobs.json" file
$ python3 jits.py display -s "nviso" # This will display the jobs from "nviso" from the jobs.json" file
```

Finally, (only for display), you can filter the results with a keyword :
```bash
$ python3 jits.py display -k "sec" # Filter the display with the "sec" keyword
```

You can, of course, combine both arguments.
```bash
$ python3 jits.py display -s "nviso" -k "sec"
```

## Contributing
You can contribute to this project from different aspects :
1. Create an issue with the error documentation
2. Create an issue with a new website implementation request (choice is left to my person)
3. Create a pull request with improvements/bug fixes
4. Create a pull request with a new website support

### Implement a new website support
In order to successfully create a pull requests (this is, to get better chance of being merged):
1. Create a new python file in the "orgs" folder with the name of the organization
2. Add the name of the company in the "common.py" file. `from . import <org_name>`
3. Implement the "scrape" method with bs4 and requests/selenium returning a list containing all jobs title (lowercase only)

Here's a simple example with the fictive company "Easy IT".
```python
# FILE - orgs/common.py
...
from . import easy_it
...
```

```python
# FILE - orgs/easy_it.py
import request # or selenium
from bs4 import BeautifulSoup

def scrape():
	# Do the jobs scraping (lowercase only)

	return new_jobs
```

## Authors
I am the only writter of this tool. If you want to know a bit more about me, do not hesite to check out my other projects or even my [website](https://www.maximilien-laenen.be).

The list of people that contributed will be populated here as this project goes on.

## License
This project is under the MIT License - see the LICENSE.md file for details