from pyeasyga import pyeasyga
from pandas import DataFrame

# setup data
# data = [{'name': 'box1', 'value': 4, 'weight': 12},
#         {'name': 'box2', 'value': 2, 'weight': 1},
#         {'name': 'box3', 'value': 10, 'weight': 4},
#         {'name': 'box4', 'value': 1, 'weight': 1},
#         {'name': 'box5', 'value': 2, 'weight': 2}]
def getRes():
	file = open("18.txt")
	str = file.readline()
	all_weight, all_capacity = str.split()
	all_weight = int(all_weight)
	all_capacity = int(all_capacity)
	# print(all_capacity, all_weight)
	# str = file.readline()
	data = []
	predata = file.readlines()
	for i in predata:
		a,b,c = i.split()
		data.append({"weight":float(a), "capacity":float(b), "value":float(c)})
	# print(data)



	ga = pyeasyga.GeneticAlgorithm(data, population_size=200, generations=100)        # initialise the GA with data

	# define a fitness function
	def fitness(individual, data):
		values, weights, capasities = 0, 0, 0
		for selected, box in zip(individual, data):
			if selected:
				capasities += box.get('capacity')
				values += box.get('value')
				weights += box.get('weight')
		if weights > all_weight or capasities > all_capacity:
			values = 0
		return values

	ga.fitness_function = fitness               # set the GA's fitness function

	maxx = 0
	a = []
	for i in range(1,15):
		ga.run()                                    # run the GA
		b, c = ga.best_individual()   # print the GA's best solution
		if b > maxx:
			maxx = b
			a = c
	value = 0
	volume = 0
	weight = 0
	items = []


	for i in range(len(a)):
		if a[i] == 1:
			value += data[i]['value']
			volume += data[i]['capacity']
			weight += data[i]['weight']
			items.append(i)


	return {"value" : int(value), "weight": int(weight), "volume": int(volume), "items" : items}



# best sol:
# 12 13000
# [{'capacity': 0.6, 'weight': 873.0, 'value': 102.0}, {'capacity': 1.1, 'weight': 1054.0, 'value': 296.0}, {'capacity': 0.6, 'weight': 1287.0, 'value': 123.0}, {'capacity': 0.8, 'weight': 776.0, 'value': 184.0}, {'capacity': 0.8, 'weight': 1445.0, 'value': 376.0}, {'capacity': 0.9, 'weight': 1054.0, 'value': 362.0}, {'capacity': 0.6, 'weight': 750.0, 'value': 183.0}, {'capacity': 0.6, 'weight': 1463.0, 'value': 302.0}, {'capacity': 1.1, 'weight': 460.0, 'value': 337.0}, {'capacity': 0.8, 'weight': 560.0, 'value': 119.0}, {'capacity': 0.5, 'weight': 1285.0, 'value': 205.0}, {'capacity': 0.7, 'weight': 1084.0, 'value': 347.0}, {'capacity': 0.5, 'weight': 253.0, 'value': 295.0}, {'capacity': 0.7, 'weight': 377.0, 'value': 103.0}, {'capacity': 0.6, 'weight': 1035.0, 'value': 203.0}, {'capacity': 0.9, 'weight': 861.0, 'value': 327.0}, {'capacity': 0.7, 'weight': 212.0, 'value': 184.0}, {'capacity': 0.5, 'weight': 1534.0, 'value': 361.0}, {'capacity': 1.1, 'weight': 575.0, 'value': 201.0}, {'capacity': 0.7, 'weight': 815.0, 'value': 307.0}, {'capacity': 0.4, 'weight': 147.0, 'value': 138.0}, {'capacity': 0.4, 'weight': 898.0, 'value': 121.0}, {'capacity': 0.6, 'weight': 325.0, 'value': 340.0}, {'capacity': 1.2, 'weight': 466.0, 'value': 114.0}, {'capacity': 1.0, 'weight': 978.0, 'value': 234.0}, {'capacity': 0.5, 'weight': 1686.0, 'value': 202.0}, {'capacity': 0.5, 'weight': 312.0, 'value': 315.0}, {'capacity': 1.1, 'weight': 503.0, 'value': 119.0}, {'capacity': 1.1, 'weight': 1406.0, 'value': 329.0}]
# (4494.0, [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1])

