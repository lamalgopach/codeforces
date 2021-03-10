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
				first_set, second_set = None, None
				first_set = cities_dict.get(neighbours[0])
				second_set = cities_dict.get(neighbours[1])
				if first_set != second_set:
					union_set = first_set.union(second_set) 
					for c_i in first_set:
						cities_dict[c_i] = union_set
					for c_i in second_set:
						cities_dict[c_i] = union_set

					road_num += 1
					lib_num -= 1

			elif neighbours[0] in cities_set or neighbours[1] in cities_set:

				road_num += 1

				present_neighbour = neighbours[0] if neighbours[0] in cities_set else neighbours[1]
				unpresent_neighbour = neighbours[0] if neighbours[0] not in cities_set else neighbours[1]
				cities_set.add(unpresent_neighbour)


				cities_dict[present_neighbour].add(unpresent_neighbour)
				set_present = cities_dict.get(present_neighbour)
				for c_i in set_present:
					cities_dict[c_i] = set_present

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
