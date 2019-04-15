import sys

year = sys.argv[1]
encoded_pattern = sys.argv[2]

separate_for_users = encoded_pattern.split(")")[1]
users = separate_for_users.split(" ")

fdemogs = open("../csv/demographics.csv")

users_all = {}
for line in fdemogs:
	line = line.strip()
	parts = line.split(",")
	users_all[parts[1]]=line

for user in users:
	if user != "":
		try:
			real_id = int(user) + 1000
			print users_all[str(real_id)]
		except:
			continue