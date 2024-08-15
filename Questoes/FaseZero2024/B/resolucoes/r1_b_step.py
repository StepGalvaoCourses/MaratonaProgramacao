def get_inputs():
    return tuple(map(int,input().split(" ")))

# Catching  the first line
num_cities, num_paths, num_parties = get_inputs()

paths_list = []

# Catching the next lines.
for i in range(num_paths):
    city1, city2, hours = get_inputs()
    paths_list.append((city1, city2, hours))

# To sort by hour 
paths_list = sorted(paths_list,key=lambda it: it[2])

visted = []
max_hour = paths_list[0][2]

for it in paths_list:
    max_hour = it[2]
    if not it[0] in visted: visted.append(it[0])
    if not it[1] in visted: visted.append(it[1])

    if(len(visted) == num_parties):
        break

print(f"Result = {max_hour}")
print(f"Sorted path list = {paths_list}")
print(f"Visted cities= {visted}")