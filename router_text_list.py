routers = []

with open('C:/pythontest/Lib/cisco_routers.txt') as file:
	for line in file:
		routers.append(line.rstrip())
		

