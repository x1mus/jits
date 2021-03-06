import argparse, sys, glob
from orgs import common


class Jits:
	def __init__(self):
		# Getting the list of sites from the filenames in the "orgs" folder
		self.website_list = [s[5:-3] for s in glob.glob("orgs/*.py")]
		self.website_list.remove("common")
		
		parser = argparse.ArgumentParser(
		description="Scrape IT job offers",
		usage="""jits.py <command> [<args>]

The most commonly used commands are:
	scrape		Run the scraping
	display		Display job offers
	info		Display the implemented websites
""")
		parser.add_argument("command", help="Subcommand to run")
		args = parser.parse_args(sys.argv[1:2])
		
		if args.command == "scrape":
			self.scrape()
		elif args.command == "display":
			self.display()
		elif args.command == "info":
			print("Implemented websites :")
			for e in self.website_list:
				print(f"- {e}")
		else:
			print("Unrecognized command")
			parser.print_help()
			exit(1)

	def scrape(self):
		parser = argparse.ArgumentParser(description="Run the scraping")
		parser.add_argument("--site", "-s", type=str, help="Target a specific website")
		args = parser.parse_args(sys.argv[2:])
		
		if args.site in self.website_list:
			try:
				common.scrape(args.site)
			except:
				print(f"An error occured while scraping {args.site}")
		else:
			for s in self.website_list:
				try:
					common.scrape(s)
				except:
					print(f"An error occured while scraping {s}")

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