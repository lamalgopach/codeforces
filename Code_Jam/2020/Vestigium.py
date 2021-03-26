def count_trace(matrix, n):
	trace = 0
	for i in range(n):
		trace += matrix[i][i]
	return trace

def count_rows_and_columns(matrix, n):
	rows = 0
	cols = 0
	for i, lst in enumerate(matrix):
		lst_set = set(lst)
		if len(lst_set) < len(lst):
			rows += 1
		col_set = set()
		for j in range(n):
			if matrix[j][i] in col_set:
				cols += 1
				break
			col_set.add(matrix[j][i])
			
	return rows, cols

t = int(input())
for i in range(t):
	n = int(input())
	matrix = []
	for j in range(n):
		lst = list(map(int,input().split()))
		matrix.append(lst)
	k = count_trace(matrix, n)
	r, c = count_rows_and_columns(matrix, n)
	print(f"Case #{i + 1}: {k} {r} {c}")