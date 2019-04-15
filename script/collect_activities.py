import operator
import sys

# f = open("publications.csv")
year = sys.argv[1]
f = open("../csv/act"+year+".csv")

fout_activities = open("../csv/activities"+year+".csv","w")
fout_conf_mapping = open("../csv/conference_mapping"+year+".csv","w")
fout_kw_mapping = open("../csv/topic_mapping"+year+".csv","w")

confs = []
all_kws = []

conf_codes = {}
kw_codes = {}
conf_cnt = 20000
kw_cnt = 10000

for line in f:
	line = line.strip()
	parts = line.split(",")
	conf = parts[2].strip()
	kws = parts[6].strip()
	author_id = parts[0]
	if author_id[0] == "a":
		continue
	if conf != "" and conf.isdigit() == False:
		if conf not in confs:
			confs.append(conf)
			conf_codes[conf] = int(conf_cnt)
			fout_activities.write(author_id+","+str(conf_cnt)+"\n")
			conf_cnt += 1
		else:
			fout_activities.write(author_id+","+str(conf_codes[conf])+"\n")
	kws_parts = kws.split(":")
	for kw in kws_parts:
		kw = kw.strip()
		if kw =="" or kw.isdigit() == True:
			continue
		if kw not in all_kws:
			all_kws.append(kw)
			kw_codes[kw]=int(kw_cnt)
			fout_activities.write(author_id+","+str(kw_cnt)+"\n")
			kw_cnt += 1
		else:
			fout_activities.write(author_id+","+str(kw_codes[kw])+"\n")

# sorted_conf_codes = sorted(conf_codes.items(), key=operator.itemgetter(1))
fout_conf_mapping.write("code,title\n")
for element in conf_codes:
	fout_conf_mapping.write(str(conf_codes[element])+","+element+"\n")

# sorted_kw_codes = sorted(kw_codes.items(), key=operator.itemgetter(1))
fout_kw_mapping.write("code,title\n")
for element in kw_codes:
	fout_kw_mapping.write(str(kw_codes[element])+","+element+"\n")