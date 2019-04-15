import sys

year = sys.argv[1]
encoded_pattern = sys.argv[2]

separate_for_items = encoded_pattern.split("(")[0]
separate_for_users = encoded_pattern.split(")")[1]
items = separate_for_items.split(" ")
users = separate_for_users.split(" ")

fconf = open("../csv/conference_mapping"+year+".csv")
ftopic = open("../csv/topic_mapping"+year+".csv")
fdemogs = open("../csv/demographics.csv")

confs = {}
for line in fconf:
	line = line.strip()
	parts = line.split(",")
	confs[parts[0]]=parts[1]

topics= {}
for line in ftopic:
	line = line.strip()
	parts = line.split(",")
	topics[parts[0]]=parts[1]

users_all = {}
for line in fdemogs:
	line = line.strip()
	parts = line.split(",")
	users_all[parts[1]]=parts[0]


for item in items:
	try:
		if int(item) < 20000:
			print topics[item]+",",
		else:
			print confs[item]+",",
	except:
		continue

print

for user in users:
	if user != "":
		try:
			real_id = int(user) + 1000
			print users_all[str(real_id)]+",",
		except:
			continue