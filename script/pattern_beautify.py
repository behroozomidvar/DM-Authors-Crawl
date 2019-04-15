for year in range(2006,2017):
	f = open("../patterns/patterns"+str(year)+".csv")
	fout = open("../patterns/patterns"+str(year)+"out.csv","w")
	for line in f:
		new_line = line.replace(")\n", ")")
		fout.write(new_line)
	f.close()
	fout.close()