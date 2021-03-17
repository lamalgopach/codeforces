def gridChallenge(grid):

	n = len(grid)
	grid_nums = []

	for i in range(n):
		nums = []
		for j in range(len(grid[i])):
			nums.append(ord(grid[i][j]) - 96)
		nums = sorted(nums)
		grid_nums.append(nums)

	for i, lst in enumerate(grid_nums):
		if i == 0:
			continue
		for j in range(len(lst)):
			if lst[j] < grid_nums[i - 1][j]:
				return "NO"
	return "YES"




t = int(input())
for i in range(t):
	n = int(input())
	grid = []
	for j in range(n):
		row = input()
		grid.append(row)
	print(gridChallenge(grid))
