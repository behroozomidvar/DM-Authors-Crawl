import sys

def set_intersect(a, b):
    out = list(set(a) & set(b))
    return len(out)

year = sys.argv[1]
next_year = str(int(sys.argv[1])+1)
encoded_pattern = sys.argv[2]

separate_for_items = encoded_pattern.split("(")[1]
items = separate_for_items.split(" ")

max_sim = 0
max_sim_group = ""

f = open("../patterns/patterns"+next_year+"out.csv")
for line in f:
	biggest_size = 0
	line = line.strip()
	this_items_sep = line.split("(")[1]
	this_items = this_items_sep.split(" ")
	nb_common = set_intersect(this_items,items)
	if len(this_items) > len(items):
		biggest_size = len(this_items)
	else:
		biggest_size = len(items)
	sim = float(nb_common) / float(biggest_size)
	if sim > max_sim:
		max_sim = sim
		max_sim_group = line

print max_sim
print max_sim_group