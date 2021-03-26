def create_str_with_parentheses(string):
	new_string = ""
	par_balance = 0
	for i, s in enumerate(string):
		if int(s) > par_balance:
			for j in range(int(s) - par_balance):
				new_string += "("
			par_balance += int(s) - par_balance
		new_string += s

		if i == len(string) - 1:
			for i in range(par_balance):
				new_string += ")"
		elif int(string[i + 1]) < int(s):
			for j in range(int(s) -  int(string[i + 1])):
				new_string += ")"
			par_balance -= int(s) -  int(string[i + 1])

	return new_string

t = int(input())
for i in range(t):
	string = input()
	new_string = create_str_with_parentheses(string)
	print(f"Case #{i + 1}: {new_string}")

# 4
# 12345
# 34015
# 23621
# 92317

# 1
# 12345



