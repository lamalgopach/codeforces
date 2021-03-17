def minimumAbsoluteDifference(arr):
	arr = sorted(arr)
	diff = set()

	for i, num in enumerate(arr):
		if i == 0:
			continue
		d = num - arr[i - 1]
		diff.add(d)
	return min(diff)







n = int(input())
arr = list(map(int, input().split()))
print(minimumAbsoluteDifference(arr))