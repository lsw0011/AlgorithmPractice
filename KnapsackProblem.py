
import time
def dict_make(file):
	classes = []
	working_dict = []
	f = open(file, "r")
	lines = f.readlines()
	itr = 0
	for line in lines:
		info = (line[0:-1]).split(",")
		classes.append(info)
		info[0] = itr					#numbers them instead of using classname
		info[1] = int(info[1])
		info[2] = int(info[2])
		itr += 1						
		working_dict.append(info)

	return working_dict, classes

working_dict, classes = dict_make('classes.txt')

def scheduler(working_dict, total_weight):

	memo = {}
	index = len(working_dict)
	print(dynamo(index-1, working_dict, total_weight, memo, 0))
	print(working_dict[0:21])

def dynamo(index, working_dict, available_weight, memo, path):
	print(bin(path))
	try:
		info = (index, available_weight)
		test = memo[info]
		return test
	except:
		if index < 0:
			return 0
		without_i = dynamo(index-1, working_dict,available_weight, memo, path)  #0
		item_weight = working_dict[index][2]
		item_value = working_dict[index][1]
		if available_weight >= item_weight: #true
			path += 2**index
			with_i = item_value + dynamo(index-1, working_dict, available_weight-item_weight, memo, path)
		else:
			return without_i
		if without_i >= with_i:
			memo[(index, available_weight)] = without_i
			return without_i
		else:
			memo[(index, available_weight)] = with_i
			return with_i

scheduler(working_dict, 40)
print(len('0b11111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))