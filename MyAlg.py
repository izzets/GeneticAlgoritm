class organs_dict:
	max_weight = 0
	max_capacity = 0
	data = []

	def __init__(self):
		file = open("18.txt")
		all_weight, all_capacity = file.readline().split()
		self.max_weight = int(all_weight)
		self.max_capacity = int(all_capacity)
		# print(all_capacity, all_weight)
		# str = file.readline()
		# data = []
		predata = file.readlines()
		for i in predata:
			a, b, c = i.split()
			self.data.append({"weight": float(a), "capacity": float(b), "value": float(c)})

class creature:
	organs = []
	weight = 0
	capacity = 0
	value = 0

	def __str__(self):
		return "weight : {}, capacity: {}, value: {} \n {}".format(self.weight,self.capacity,self.value,self.organs)
	def __lt__(self, other):
		return self.value < other.value
	def __le__(self, other):
		return self.value <= other.value
	def __eq__(self, other):
		return self.value == other.value
	def __ne__(self, other):
		return self.value != other.value
	def __ge__(self, other):
		return self.value >= other.value
	def __gt__(self, other):
		return self.value > other.value


	def __init__(self, organs):
		self.organs = organs
		self.calc_weight()
		self.calc_capacity()
		self.calc_value()

	def calc_weight(self):
		for i in range(len(self.organs)):
			if self.organs[i] == 1:
				self.weight += organs_dict.data[i]['weight']

	def calc_capacity(self):
		for i in range(len(self.organs)):
			if self.organs[i] == 1:
				self.capacity += organs_dict.data[i]['capacity']

	def calc_value(self):
		self.value = 0
		if (self.weight <= organs_dict.max_weight) and (self.capacity <= organs_dict.max_capacity):
			for i in range(len(self.organs)):
				if self.organs[i] == 1:
					self.value += organs_dict.data[i]['value']
		else:
			self.value = 0

	def mutation(self):
		for i in range(len(self.organs)):
			self.organs[i] ^= 1
		self.calc_value()
		if self.value == 0:
			for i in range(len(self.organs)):
				self.organs[i] ^= 1
			self.calc_value()



import random

class population:
	creatures = []
	population_length = 4

	def __str__(self):

		res = ""
		for i in range(self.creatures.__len__()):
			res += str(self.creatures[i]) + "\n"
		return res

	def __init__(self, population_length):
		self.population_length = population_length
		r = random.Random()
		llen = organs_dict.data.__len__()
		while self.creatures.__len__() < self.population_length:
			bin_a = [round(r.uniform(0, 1)) for _ in range(llen)]
			cre = creature(bin_a)
			if cre.value != 0:
				self.creatures.append(cre)

	def love(self, mommy, daddy, amount_of_childs):
		childs = []
		for i in range(amount_of_childs):
			a = self.cross_random(mommy, daddy)
			cre = creature(a)
			if cre.value > 0:
				childs.append(cre)
		return childs

	@staticmethod
	def cross_points(mommy, daddy):
		r = random.Random()
		points = list()
		points.append(0)
		points.append(r.uniform(1, len(mommy.organs)))
		points.append(len(mommy.organs))
		points.sort()
		res_organs = []
		mommy_or_daddy = 0
		for j in range(len(points)-1):
			mommy_or_daddy ^= 1
			for i in range(points[j],points[j+1]):
				if mommy_or_daddy == 1:
					res_organs.append(mommy.organs[i])
				else:
					res_organs.append(daddy.organs[i])
		return res_organs

	@staticmethod
	def cross_random(mommy, daddy):
		res_organs = []
		r = random.Random()
		mommy_or_daddy = 0
		for i in range(0, len(mommy.organs)):

			if r.random() > 0.5:
				res_organs.append(mommy.organs[i])
			else:
				res_organs.append(daddy.organs[i])
		return res_organs

	def generation(self):
		r = random.Random()
		new_creatures = self.creatures
		self.creatures.sort(reverse=True)
		creatures_to_reproduce = []
		for i in range(int(self.creatures.__len__()*0.2)):
			creatures_to_reproduce.append(self.creatures[i])
		while creatures_to_reproduce.__len__() > 1:
			mom = creatures_to_reproduce[int(r.uniform(0,creatures_to_reproduce.__len__()))]
			creatures_to_reproduce.remove(mom)
			dad = creatures_to_reproduce[int(r.uniform(0,creatures_to_reproduce.__len__()))]
			creatures_to_reproduce.remove(dad)
			new = self.love(mom,dad,2)
			for i in range(new.__len__()):
				new_creatures.append(new[i])
		amount_of_mutations = 5
		for i in range(amount_of_mutations):
			new_creatures[int(r.uniform(0,new_creatures.__len__()))].mutation()
		new_creatures.sort(reverse=True)
		self.creatures = new_creatures[0:self.creatures.__len__()]

maxx = 0
organs_dict = organs_dict()
for i in range(15):
	_a = population(200)
	_a.creatures.sort(reverse=True)
	# print(_
	for _ in range(20):
		_a.generation()
	if (_a.creatures[0].value > maxx):
		maxx = _a.creatures[0].value
		max_a = _a.creatures[0]


items = []
for ii in range(len(max_a.organs)):
	items.append(ii)

import requests as re
import json
import LibAlg

headers = {'content-type': 'application/json'}
url = 'https://cit-home1.herokuapp.com/api/ga_homework'

data = {}
data["2"] = {"value" :int(max_a.value), "weight": int(max_a.weight), "volume": int(max_a.capacity), "items": items}
data["1"] = LibAlg.getRes()


r = re.post(url, data=json.dumps(data), headers=headers)
print(r)
print(r.text)







# best solution
# weight : 6280.0, capacity: 7.5, value: 4820.0
#  [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]