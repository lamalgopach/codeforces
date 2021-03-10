# Challenge from Hackerrank

# Determine the minimum cost to provide library access to all citizens of HackerLand. 
# There are n cities numbered from 1 to n. 
# Currently there are no libraries and the cities are not connected. 
# Bidirectional roads may be built between any city pair listed in cities. 

# A citizen has access to a library if:
# -Their city contains a library.
# -They can travel by road from their city to a city containing a library.

# Input:

# The first line contains a single integer q, that denotes the number of queries.
# The subsequent lines describe each query in the following format:
# - The first line contains four space-separated integers that describe the respective 
# values of n, m, c_lib, c_road - 
# the number of cities, number of roads, cost of a library and cost of a road.

# - Each of the next m lines contains two space-separated integers, u[i] and v[i], 
# that describe a bidirectional road that can be built to connect cities u[i] and v[i].


# Output:
# int: the minimal cost


def modify_dict(old_set, new_set, dict_):
	for i in old_set:
		dict_[i] = new_set
	return dict_



def roadsAndLibraries(n, c_lib, c_road, cities):
	if c_lib <= c_road:
		return c_lib * n
	else:
		road_num = 0
		lib_num = 0

		cities_set = set()
		cities_dict = {}

		for neighbours in cities:
			if len(cities_set) == n and len(cities_dict) == 1:
				break
			elif len(cities_set) == n and len(cities_dict) == n:
				break

			if neighbours[0] in cities_set and neighbours[1] in cities_set:
				first_set = cities_dict.get(neighbours[0])
				second_set = cities_dict.get(neighbours[1])

				if first_set != second_set:
					union_set = first_set.union(second_set) 

					cities_dict = modify_dict(first_set, union_set, cities_dict)
					cities_dict = modify_dict(second_set, union_set, cities_dict)

					road_num += 1
					lib_num -= 1

			elif neighbours[0] in cities_set or neighbours[1] in cities_set:
				old_neighbour = neighbours[0] if neighbours[0] in cities_set else neighbours[1]
				new_neighbour = neighbours[0] if neighbours[0] not in cities_set else neighbours[1]
				cities_set.add(new_neighbour)
				cities_dict[old_neighbour].add(new_neighbour)

				old_set = cities_dict.get(old_neighbour)
				new_set = old_set 

				cities_dict = modify_dict(old_set, new_set, cities_dict)

				road_num += 1

			elif neighbours[0] not in cities_set and neighbours[1] not in cities_set:

				road_num += 1
				lib_num += 1

				cities_set.add(neighbours[0])
				cities_set.add(neighbours[1])

				cities_dict[neighbours[0]] = set()
				cities_dict[neighbours[0]].add(neighbours[0])
				cities_dict[neighbours[0]].add(neighbours[1])
				cities_dict[neighbours[1]] = cities_dict.get(neighbours[0])

	lib_num += n - len(cities_set)

	return road_num * c_road + lib_num * c_lib

q = int(input())
for i in range(q):

	n, m, c_lib, c_road = map(int, input().split())

	cities = []

	for j in range(m):
		c1_c2 = list(map(int, input().split()))
		cities.append(c1_c2)
	print(roadsAndLibraries(n, c_lib, c_road, cities))
