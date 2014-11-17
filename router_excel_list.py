import csv

routers = []

with open('C:/Users/adraper/Documents/ciscorouters.csv') as file:
	
	csv_list  = list(csv.reader(file))

	for list in csv_list:
		routers.append(list[0])
	



