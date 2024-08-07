with open("Downloads/input.txt") as f:
	highest1 = 0
	highest2 = 0
	highest3 = 0
	current = 0
	lines = f.readlines()
	for line in lines:
		if line != '\n':
			current = current + int(line)
			print("current = ", current)
		elif line == '\n' or '':
			if current > highest1:
				highest3 = highest2
				highest2 = highest1
				highest1 = current
				print("highest1 = ", current)
			elif current > highest2:
				highest3 = highest2
				highest2 = current
				print("highest2 = ", current)
			elif current > highest3:
				highest3 = current
				print("highest3 = ", current)
			current = 0
	print(highest1, highest2, highest3)
	print(highest1+highest2+highest3)
		
