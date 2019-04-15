# this script crawls top-tier conferences from 2006 to 2016 to obtain a list of authors contributing to databases.

from __future__ import unicode_literals
from pattern.web import URL
import urllib2
from bs4 import BeautifulSoup
from unidecode import unidecode

conferences = ["WWW","VLDB","SIGMOD","ICWSM","ICDE","SIGIR","CIKM","DEXA1","DEXA2","DEXA3","RecSys","EDBT"]

# The substring REPLACE should be replaced by year
conference_link={}
conference_link["WWW"]="http://dblp.uni-trier.de/db/conf/www/wwwREPLACE.html"
conference_link["VLDB"]="http://dblp.uni-trier.de/db/journals/pvldb/pvldbREPLACE.html"
conference_link["SIGMOD"]="http://dblp.uni-trier.de/db/conf/sigmod/sigmodREPLACE.html"
conference_link["ICWSM"]="http://dblp.uni-trier.de/db/conf/icwsm/icwsmREPLACE.html"
conference_link["ICDE"]="http://dblp.uni-trier.de/db/conf/icde/icdeREPLACE.html"
conference_link["SIGIR"]="http://dblp.uni-trier.de/db/conf/sigir/sigirREPLACE.html"
conference_link["CIKM"]="http://dblp.uni-trier.de/db/conf/cikm/cikmREPLACE.html"
conference_link["DEXA1"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE.html"
conference_link["DEXA2"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE-1.html"
conference_link["DEXA3"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE-2.html"
conference_link["RecSys"]="http://dblp.uni-trier.de/db/conf/recsys/recsysREPLACE.html"
conference_link["EDBT"]="http://dblp.uni-trier.de/db/conf/edbt/edbtREPLACE.html"

# the year that each confernce has begun. We are interested to 2006-2016.
conference_first_year={}
conference_first_year["WWW"]=2006
conference_first_year["VLDB"]=2008
conference_first_year["SIGMOD"]=2006
conference_first_year["ICWSM"]=2007
conference_first_year["ICDE"]=2006
conference_first_year["SIGIR"]=2006
conference_first_year["CIKM"]=2006
conference_first_year["RecSys"]=2007
conference_first_year["EDBT"]=2008
conference_first_year["DEXA2"]=2010
conference_first_year["DEXA3"]=2010
conference_first_year["DEXA1"]=2007

conference_last_year={}
conference_last_year["WWW"]=2016
conference_last_year["VLDB"]=2016
conference_last_year["SIGMOD"]=2016
conference_last_year["ICWSM"]=2016
conference_last_year["ICDE"]=2016
conference_last_year["SIGIR"]=2016
conference_last_year["CIKM"]=2016
conference_last_year["RecSys"]=2016
conference_last_year["EDBT"]=2016
conference_last_year["DEXA2"]=2016
conference_last_year["DEXA3"]=2016
conference_last_year["DEXA1"]=2009

# out file
fout = open("../csv/authors.csv","w")

# print header
fout.write("author_name, dblp_link, seen_in_conf, year\n")

for conference in conferences:
	for year in range(conference_first_year[conference],conference_last_year[conference]+1):
		current_link = ""
		if conference == "VLDB":
			current_link = conference_link[conference].replace("REPLACE",str(year-2006))
		else:
			current_link = conference_link[conference].replace("REPLACE",str(year))
		current_page = urllib2.urlopen(current_link).read()
		soup = BeautifulSoup(current_page)
		author_spans = soup.findAll('span', itemprop="author", itemtype="http://schema.org/Person")
		for author_span in author_spans:
			author_internal_part = author_span('a')[0]
			author_link = author_internal_part["href"]
			author_name = unidecode(author_internal_part("span")[0].string)
			author_name = author_name.replace(",","")
			reported_conference = conference
			if conference[0:4]=="DEXA":
				reported_conference = "DEXA"
			# print author_name+", "+author_link+", "+reported_conference+", "+str(year)
			fout.write(author_name+", "+author_link+", "+reported_conference+", "+str(year)+"\n")
		print "done with "+conference+" "+str(year)
# for conf in range(0,11):
# 	base_url=init_url+conferences[conf]
# 	for year in range(2004, 2014):
# 		url=base_url+str(year)+'.html'
# 		try:
# 			page = urllib2.urlopen(url).read()
# 		except urllib2.HTTPError:
# 			continue
# 		print year,conferences[conf]
# 		soup = BeautifulSoup(page)
# 		data = soup.find_all("div", { "class" : "data" })
# 		length = len(data)
# 		for i in range(0, length):
# 			# get authors
# 			authors=data[i].find_all("a")
# 			lengthA=len(authors)
# 			if lengthA>0:
# 				for j in range(0, lengthA-1):
# 					author=''.join(authors[j].findAll(text=True))
# 					author=author.encode("utf-8")
# # 					print author
# 				author=''.join(authors[lengthA-1].findAll(text=True))
# 				author=author.encode("utf-8")
# # 				print author
# 			else:
# 				continue
		
	
