import sys

def set_intersect(a, b):
    out = list(set(a) & set(b))
    return out

def set_union(a, b):
    out = list(set(a) | set(b))
    return out

year = sys.argv[1]
next_year = str(int(sys.argv[1])+1)
encoded_pattern = sys.argv[2]

separate_for_users = encoded_pattern.split(")")[1]
users = separate_for_users.split(" ")

max_sim = 0
max_sim_group = ""
max_sim_users = []

f = open("../patterns/patterns"+next_year+"out.csv")
for line in f:
	biggest_size = 0
	line = line.strip()
	this_users_sep = line.split(")")[1]
	this_users = this_users_sep.split(" ")
	nb_common = len(set_intersect(this_users,users))
	if len(this_users) > len(users):
		biggest_size = len(this_users)
	else:
		biggest_size = len(users)
	sim = float(nb_common) / float(biggest_size)
	if sim > max_sim:
		max_sim = sim
		max_sim_group = line
		max_sim_users = this_users

# print max_sim
print max_sim_group

# difference
print "*** Difference (membership) ***"
intersect = set_intersect(max_sim_users,users)
union = set_union(max_sim_users,users)
difference = [x for x in union if x not in intersect]
print difference


