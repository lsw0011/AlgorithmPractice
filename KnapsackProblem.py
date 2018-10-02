
import time
def dict_make(file):
	working_dict = []
	f = open(file, "r")
	lines = f.readlines()
	itr = 0
	for line in lines:
		info = (line[0:-1]).split(",")
		info[1] = int(info[1])
		info[2] = int(info[2])						
		working_dict.append(info)

	return working_dict

working_dict = dict_make('classes.txt')

def scheduler(working_dict, total_weight):

	memo = {}
	index = len(working_dict)
	res = dynamo(index-1, working_dict, total_weight, memo, 0)
	print(getClasses(working_dict, res[1]))

def getClasses(working_dict, path):
	itr = 0
	classes = []
	while path > 0:
		rmdr = path%2
		if rmdr == 1:
			classes.append(working_dict[itr])
		path = path//2
		itr += 1
	return classes

def dynamo(index, working_dict, available_weight, memo, path):
	try:
		info = (index, available_weight)
		test = memo[info]
		return test
	except:
		if index < 0:
			return 0, 0
		without_i = dynamo(index-1, working_dict,available_weight, memo, path)  #0
		item_weight = working_dict[index][2]
		item_value = working_dict[index][1]
		if available_weight >= item_weight: #true
			prev = dynamo(index-1, working_dict, available_weight-item_weight, memo, path)
			path = 2**index + prev[1]
			value = item_value + prev[0]
			with_i = value, path
		else:
			return without_i
		if without_i[0] >= with_i[0]:
			memo[(index, available_weight)] = without_i
			return without_i
		else:
			memo[(index, available_weight)] = with_i
			return with_i
scheduler(working_dict, 40)