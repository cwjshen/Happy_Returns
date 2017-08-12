# Part A
# Remove Dupes

def remove_dupes(array):
	seen_set = set()
	i = 0
	while i < len(array) :
		print i, array, seen_set
		if array[i] in seen_set:
			del array[i]
			i = i - 1
		else:
			seen_set.add(array[i])

		i = i + 1

	print 'Final Array: ', array
	return array


# Part B
# Remove Second Dupe
# I did this by taking advantage of the difference between Python's remove() and del
# Wasn't quite sure how to do it in place without using remove/del
# Alternatively maybe could've built a new solution array, inserting and deleting as needed

def remove_second_dupe(array):
	seen_dict = {}
	i = 0
	while i < len(array):
		print i, array, seen_dict
		if array[i] in seen_dict:
			seen_dict[array[i]] = seen_dict[array[i]] + 1
			if seen_dict[array[i]] <= 2:				
				array.remove(array[i])
				i = i - 1
			if seen_dict[array[i]] > 2:
				del array[i]
				i = i - 1
		else:
			seen_dict[array[i]] = 1


		i = i + 1

	print 'Final Array: ', array
	return array

#

def remove_nth_dupe(array, n):
	seen_dict = {}
	i = 0
	while i < len(array):
		print i, array, seen_dict
		if array[i] in seen_dict:
			seen_dict[array[i]] = seen_dict[array[i]] + 1
			if seen_dict[array[i]] <= n:				
				array.remove(array[i])
				i = i - 1
			if seen_dict[array[i]] > n:
				del array[i]
				i = i - 1
		else:
			seen_dict[array[i]] = 1


		i = i + 1

	print 'Final Array: ', array
	return array


def main():
	
	print 'PART A'
	print '======================='
	array = [1,2,1,3,2,1,7]
	two_A = remove_dupes(array)
	print 'PART B'
	print '======================='	
	array = [1,2,1,3,2,1,7]
	two_B = remove_second_dupe(array)
	print 'PART C'
	print '======================='	
	array = [1,2,1,3,2,1,7]
	two_C = remove_nth_dupe(array, 3)

main()