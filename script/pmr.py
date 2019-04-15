for year in range(2006,2017):
	year_str = str(year)
	f = open("../csv/activities"+year_str+".csv")
	user_id = {}
	for my_id in range(1000,9204):
		user_id[my_id] = ""

	for line in f:
		line = line.strip()
		parts = line.split(",")
		user_id[int(parts[0])] += parts[1] + " "

	fout = open("../pmr/pmr"+year_str+".csv","w")
	for i in range(1000,9203):
		fout.write(user_id[i]+"\n")
	fout.close()
	f.close()
