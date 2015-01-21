import csv
import re

def escape_single_quote(s):
	return re.sub("'", "\\'", s)

def get_country_name_and_code_xml(filename):
	country_names_xml = "<string-array name=\"country_names_array\">"
	country_codes_xml = "<string-array name=\"country_codes_array\">"

	with open(filename, 'r') as f:
		reader = csv.reader(f, delimiter=",")
		next(reader)

		for line in reader:
			[iso, name] = map(escape_single_quote, line)

			country_names_xml += "\n\t<item>" + name + "</item>"
			country_codes_xml += "\n\t<item>" + iso + "</item>"

	country_names_xml += "\n</string-array>"
	country_codes_xml += "\n</string-array>"

	return [country_names_xml, country_codes_xml]







