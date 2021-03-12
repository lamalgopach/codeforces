"""
Given an array B and must determine an array A. For all i, B[i] >= A[i] >= 1. Select 
a series of A[i] such that the sum of the absolute difference of consecutive pairs of A 
is maximized. This will be the array's cost.

Input:
 - t: number of test cases
 - n: length of B
 - space-separated integers of B[i]

Output:
Print the maximum sum on a separate line.
"""

def cost(b):

	sum_one = 0
	sum_num = 0	
	for i, num in enumerate(b):
		if i == 0:
			continue

		num_to_last = abs(num - b[i - 1])
		num_to_one = abs(num - 1)
		last_to_one = abs(1 - b[i - 1])

		temp = sum_one

		sum_one = sum_num + last_to_one
		sum_num = max(sum_num + num_to_last, temp + num_to_one)

	return max(sum_one, sum_num)

t = int(input())
for i in range(t):
	n = int(input())
	b = list(map(int, input().split()))
	print(cost(b))