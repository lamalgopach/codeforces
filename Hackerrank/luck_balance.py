def luckBalance(k, contests):
	
	important = []
	luck = 0

	for i, contest in enumerate(contests):
		if contest[1] > 0:
			important.append(contest[0])
		else:
			luck += contest[0]
	important = sorted(important)
	for i in range(len(important) - 1, -1, -1):

		if i > len(important) - 1 - k:
			luck += important[i]
		else:
			luck -= important[i]
	return luck




n, k = map(int, input().split())
contests = []
for i in range(n):
	l, t = list(map(int, input().split()))
	contests.append([l, t])
print(luckBalance(k, contests))
