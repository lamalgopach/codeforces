def is_palindromic(lst, n):

	
	#check how many different numbers could be in the n-matrix
	len_set = len(set(lst))
	set_ = set(lst)
	
	if n%2 == 0:
		a = n*n/4
	else:
		a = (n+1)*(n+1)/4

	if len_set > a:
		print("NO")
		return

	if len(lst) != n*n:
		print("no")
		return

	#dictionary with a number of different numbers
	dict_ = {}
	for i in lst:
		if i not in dict_:
			dict_[i] = 1
		else:
			dict_[i] += 1

	#check if the number of different numbers are ok for the n-matrix

	#n=1, always ok, print and return
	if n == 1:
		print('YES')
		# print(' '.join(map(str, lst)))
		matrix = print_matrix(dict_, n)
		return matrix

	# n=2, ok only when all numbers the same, we check it before(len set)
	elif n == 2:
		print("YES")
		for i in range(n):
			# print(' '.join(map(str, lst[i:i+2])))
			matrix = print_matrix(dict_, n)
			return matrix

	# n: even numbers, not 2
	elif n%2 == 0 and n != 2:
		for key, value in enumerate(dict_.items()):
			if value[1] % 4 != 0:
				print("NO")
				return
		else:
			print("yes")
			matrix = print_matrix(dict_, n)
			return matrix

	elif n%2 != 0:
		ksi = n-1
		psi = 0
		for key, value in enumerate(dict_.items()):
			if value[1] % 4 != 0 and value[1] % 2 == 0:
				psi += 1
		if psi>ksi:
			print("NO")
			return

		else:
			odd = 0
			two = 0
			for key, value in enumerate(dict_.items()):
				if value[1] % 2 != 0:
					odd += 1
					if odd > 1:
						print("NO")
						return
				elif value[1] == 2:
					two += 1
					if two > n-1:
						print("no")
						return
			else:
				print("yes")
				matrix = print_matrix(dict_, n)
				return matrix

def print_matrix(dict_, n):
	
	Matrix = [[0 for x in range(n)] for y in range(n)] 

	lst_2 = []
	lst_2_2 = []
	lst_2_2_2 = []
	lst_4 = []
	odd_num = 0
	pairs_without_quarters = 0

	for key, value in enumerate(dict_.items()):

		if value[1] % 2 == 0 and value[1] % 4 != 0:
			lst_2.append(value[0])
			pairs_without_quarters += 1

		elif value[1] % 4 == 0:
			lst_4.append(value[0])
			
		else:
			odd_num += value[0]

	if n%2 != 0:
		odd_num_num = dict_[odd_num]

		if odd_num != 0:
			Matrix[n//2][n//2] = odd_num
			dict_[odd_num] -= 1

		if dict_[odd_num] == 0:
			odd_num = 0
		elif dict_[odd_num]%4 != 0:
			Matrix[n//2][(n//2)-1] = odd_num
			Matrix[n//2][(n//2)+1] = odd_num
	
			if dict_[odd_num] == 2:
				odd_num = 0
			else:
				dict_[odd_num] -= 2

		if len(lst_2) != 0:
			if len(lst_2) >= n//2:
				for i in range(n//2):
					Matrix[i][n//2] = lst_2[i]
					Matrix[n-1-i][n//2] = lst_2[i]
					dict_[lst_2[i]] -= 2

					if dict_[lst_2[i]] == 0:
						lst_2[i] = 0

			else:
				for i in range(len(lst_2)):
					Matrix[i][n//2] = lst_2[i]
					Matrix[n-1-i][n//2] = lst_2[i]
					dict_[lst_2[i]] -= 2

			for item in lst_2:

				if item > 0 and dict_[item] % 4 == 0:
					lst_4.append(item)
				elif item > 0:
					lst_2_2.append(item)

		if len(lst_2_2) != 0:

			if len(lst_2_2) >= n//2:
				for j in range(n//2):
					Matrix[n//2][j] = lst_2_2[j]
					Matrix[n//2][n-1-j] = lst_2_2[j]
					dict_[lst_2_2[j]] -= 2

					if dict_[lst_2_2[j]] == 0:
						lst_2_2[j] = 0
					
			else:
				for j in range(len(lst_2_2)):
					Matrix[n//2][j] = lst_2_2[j]
					Matrix[n//2][n-1-j] = lst_2_2[j]
					dict_[lst_2_2[j]] -= 2

			for item in lst_2_2:

				if item > 0 and dict_[item] % 4 == 0:
					lst_4.append(item)
				elif item > 0:
					lst_2_2_2.append(item)

	for i in range(n):
		
		if len(lst_4) == 0 and odd_num == 0:
				break
		for j in range(n//2+1):

			if len(lst_4) == 0 and odd_num == 0:
				break
			
			if Matrix[i][j] == 0 and len(lst_4) != 0 and n%2 == 0:

				z = dict_[lst_4[0]]//4

				ii = i
				jj = j
	
			
				while z:
					
					if Matrix[i][j] == 0:
						Matrix[i][j] = lst_4[0]
						Matrix[i][n-j-1] = lst_4[0]
						Matrix[n-i-1][j] = lst_4[0]
						Matrix[n-i-1][n-j-1] = lst_4[0]
						z -= 1
				
					if j == (n-1)//2:
						i += 1
						j = 0
						
					else:
						j += 1
				
				del lst_4[0]

				i = ii
				j = jj

			elif Matrix[i][j] == 0 and len(lst_4) != 0:

				b = dict_[lst_4[0]]
	
				z = b//4
				
				ii = i
				jj = j
		
				while z:

					
					if Matrix[i][j] == 0 and i != (n-1)//2 and j != (n-1)//2:

						Matrix[i][j] = lst_4[0]
						Matrix[i][n-1-j]= lst_4[0]
						Matrix[n-i-1][j] = lst_4[0]
						Matrix[n-i-1][n-1-j] = lst_4[0]
						z -= 1

					elif Matrix[i][j] == 0 and j == (n-1)//2 and i != ((n-1)//2)-1:

						Matrix[i][j] = lst_4[0]
						Matrix[i+1][j] = lst_4[0]
						Matrix[n-i-1][j] = lst_4[0]
						Matrix[n-i-2][j] = lst_4[0]
						z -= 1

					elif Matrix[i][j] == 0 and i == (n-1)//2:

						Matrix[i][j] = lst_4[0]
						Matrix[i][n-j-1] = lst_4[0]
						if j+1 != n-j-2:
							Matrix[i][j+1]= lst_4[0]
							Matrix[i][n-j-2] = lst_4[0]
							j += 1
						else:
							Matrix[i-1][n//2]= lst_4[0]
							Matrix[i+1][n//2] = lst_4[0]

						z -= 1
						
					
					if j == ((n-1)//2):
						
						i += 1
						j = 0
					else:
						j += 1

				i = ii
				j = jj
					
				del lst_4[0]

			elif Matrix[i][j] == 0 and odd_num != 0:

				b = dict_[odd_num]
				k = 0
				i = 0
				j = 0

				while b:
					
					if Matrix[i][j] == 0:
						Matrix[i][j] = odd_num
						b -= 1

					if j == (n-1):
						i += 1
						j = 0
					else:
						j += 1

				odd_num = 0
				
							
	for rows in Matrix:
		rows = str(rows).replace(", ", " ")
		rows = rows.strip("]")
		rows = rows.strip("[")
		print(rows)

n = int(input())
lst = list(map(int, input().split()))
is_palindromic(lst, n)