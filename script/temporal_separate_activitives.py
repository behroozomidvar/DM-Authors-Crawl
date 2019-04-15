f = open("../csv/publications.csv")

year_activity = {}
for i in range(2006,2017):
	year_activity[i] = ""

line_cnt = 0
for line in f:
	line_cnt += 1
	if line_cnt == 1:
		continue
	parts = line.split(",")
	try:
		year = int(parts[3])
		if (year < 2017 and year > 2005):
			year_activity[year] += line
	except:
		continue

for i in range(2006,2017):
	acitivity_file_name = "../csv/act"+str(i)+".csv"
	header = "author_id, paper_title, paper_conference, paper_year, nb_authors, is_first_author, topics"
	fyear = open(acitivity_file_name,"w")
	fyear.write(year_activity[i])
	fyear.close()
