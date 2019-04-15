from __future__ import unicode_literals
# from pattern.web import URL
import urllib2
from bs4 import BeautifulSoup
# from unidecode import unidecode

topics = []
topic_codes = {}
ftopics = open("../csv/db_keywords.csv")
for line in ftopics:
	line = line.strip()
	parts = line.split(",")
	topics.append(parts[1])
	topic_codes[parts[1]] = parts[0]

# publications.csv < author_id, paper_title, paper_conference, paper_year, nb_authors, is_first_author, topics (separated by ":"") >
fout1 = open("../csv/publications.csv","w")
fout1.write("author_id, paper_title, paper_conference, paper_year, nb_authors, is_first_author, topics\n")

# basic_demographics.csv < author_id, first_publication_year, number_of_publications, number_of_first_author_publications, number_of_coauthors, affiliation >
fout2 = open("../csv/basic_demographics.csv","w")
fout2.write("author_id, first_publication_year, number_of_publications, number_of_first_author_publications, number_of_coauthors, affiliation\n")

# loop on authors
f = open("../csv/authors_unique.csv")

for line in f:
	line = line.strip()
	parts = line.split(",")
	author_id = parts[0]
	dblp_link = parts[2]
	if author_id[0]=="a":
		continue
	# if int(author_id) > 10000:
	# 	exit()
	# if int(author_id) < 7000:
	# 	continue
	current_page = urllib2.urlopen(dblp_link).read()
	soup = BeautifulSoup(current_page,"html.parser")

	affiliation = ""
	affiliation_span = soup.findAll(itemprop="affiliation", itemtype="http://schema.org/Organization")
	for s in affiliation_span:
		affiliation = s.span.string
	affiliation = affiliation.replace(",","")
	
	first_publi_year = 2017

	# loop on author papers
	number_of_first_author_publications = 0
	number_of_coauthors = 0
	paper_divs = soup.findAll('div', itemprop="headline", class_="data")
	number_of_publications = str(len(paper_divs))
	for paper_div in paper_divs:
		author_spans = paper_div.findAll('span', itemprop="author", itemtype="http://schema.org/Person")
		being_first_author = author_spans[0].findAll('span', itemprop="name", class_="this-person")
		is_first_author = "false"
		if len(being_first_author) != 0:
			is_first_author = "true"
			number_of_first_author_publications += 1
		nb_authors = len(author_spans)
		number_of_coauthors += nb_authors
		paper_title = paper_div.findAll('span', itemprop="name", class_="title")
		paper_title_clean = ""
		c = paper_title[0].contents
		# try:
		for cc in c:
			temp = ""
			try:
				temp = cc.string.encode('utf-8')
				paper_title_clean += temp
			except:
				temp = ""
				paper_title_clean += temp	
		paper_title_clean = paper_title_clean[:-1].lower()
		paper_title_clean = paper_title_clean.replace(",","")
		# except:
		# 	print paper_title
		# 	print c
				
		paper_topics = ""
		for topic in topics:
			if topic in paper_title_clean:
				paper_topics += topic+":"
				
		paper_conference =""
		paper_conf_span = paper_div.findAll('span', itemprop="isPartOf")
		for s in paper_conf_span:
			l = s.findAll('span', itemprop="name")
			if len(l) > 0:
				paper_conference = l[0].string
			# if s.find("<span itemprop=\"name\">"):
			# 	print paper_conference, "**"
			# 	print s
	
		paper_year_span = paper_div.findAll('span', itemprop="datePublished")
		paper_year = paper_year_span[0].string
		
		if int(paper_year) < first_publi_year:
			first_publi_year = int(paper_year)

		final_fout1 = author_id + ", " + paper_title_clean + ", " + paper_conference + ", " + str(paper_year) + ", " + str(nb_authors) + ", " + is_first_author + ", " + paper_topics + "\n"
		final_fout1 = final_fout1.encode('utf-8')
		# print hello
		# exit()
		fout1.write(final_fout1)

	first_publication_year = first_publi_year
	fout2_final = author_id + ", " + str(first_publication_year) + ", " + str(number_of_publications) + ", " + str(number_of_first_author_publications) + ", " + str(number_of_coauthors) + ", " + affiliation + "\n"
	fout2_final = fout2_final.encode('utf-8')
	fout2.write(fout2_final)
	print author_id, "done ..."
	
