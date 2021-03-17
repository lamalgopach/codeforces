

def marcsCakewalk(calories):

	calories = sorted(calories)
	miles = 0
	k = 0

	for i in range(len(calories) - 1, -1, -1):

		miles += calories[i] * (2 ** k)
		k += 1

	return miles


n = int(input())
calories = list(map(int, input().split()))
print(marcsCakewalk(calories))