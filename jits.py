import argparse, sys
from orgs import nato, nviso, approach


class Jits:
	def __init__(self):
		self.website_list = ["nato", "nviso", "approach"]
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
			eval(args.site + ".scrape()") # Not sure about that
		else:
			for s in self.website_list:
				eval(s + ".scrape()") # Not sure about that

	def display(self):
		parser = argparse.ArgumentParser(description="Display job offers")
		parser.add_argument("--site", "-s", type=str, help="Target a specific website")
		parser.add_argument("--keyword", "-k", type=str, help="Filter on a keyword")
		args = parser.parse_args(sys.argv[2:])
		
		if args.site in self.website_list:
			if not args.keyword:
				eval(f"{args.site}.display({args.keyword})")
			else:
				eval(f"{args.site}.display('{args.keyword}')")
		else:
			for s in self.website_list:
				if not args.keyword:
					eval(f"{s}.display({args.keyword})")
				else:
					eval(f"{s}.display('{args.keyword}')")



if __name__ == "__main__":
	Jits()