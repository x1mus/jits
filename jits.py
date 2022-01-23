import argparse, sys
from orgs import common


class Jits:
	def __init__(self):
		self.website_list = ["nato", "nviso", "approach", "ictjobs"]
		parser = argparse.ArgumentParser(
		description="Scrape IT job offers",
		usage="""jits.py <command> [<args>]

The most commonly used commands are:
	scrape		Run the scraping
	display		Display job offers
""")
		parser.add_argument("command", help="Subcommand to run")
		args = parser.parse_args(sys.argv[1:2])
		
		if args.command == "scrape":
			self.scrape()
		elif args.command == "display":
			self.display()
		else:
			print("Unrecognized command")
			parser.print_help()
			exit(1)

	def scrape(self):
		parser = argparse.ArgumentParser(description="Run the scraping")
		parser.add_argument("--site", "-s", type=str, help="Target a specific website")
		args = parser.parse_args(sys.argv[2:])
		
		if args.site in self.website_list:
			common.scrape(args.site)
		else:
			for s in self.website_list:
				common.scrape(s)

	def display(self):
		parser = argparse.ArgumentParser(description="Display job offers")
		parser.add_argument("--site", "-s", type=str, help="Target a specific website")
		parser.add_argument("--keyword", "-k", type=str, help="Filter on a keyword")
		args = parser.parse_args(sys.argv[2:])
		
		if args.site in self.website_list:
			common.display(args.site, args.keyword)
		else:
			for s in self.website_list:
				common.display(s, args.keyword)


if __name__ == "__main__":
	Jits()