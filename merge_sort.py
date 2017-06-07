# merge sort 

def mergeSort(a_list):
	if len(a_list) > 1:				# makes sure the recursion stops when the length of the list is 1
		mid = len(a_list) / 2
		left_side = a_list[:mid]
		right_side = a_list[mid:]

		mergeSort(left_side)
		mergeSort(right_side)
		merge(a_list, left_side, right_side)

def merge(a_list, left_list, right_list):
	i = 0 # index for the left side of the list
	i_max = len(left_list) # length of left side
	j = 0 # index for the right side of the list
	j_max = len(right_list) # length of right side

	for list_index in range(0, len(a_list)):
		if i < i_max and j< j_max:
			if left_list[i] < right_list[j]:
				a_list[list_index] = left_list[i]
				i = i + 1
			else:
				a_list[list_index] = right_list[j]
				j = j + 1
		elif i < i_max:
			a_list[list_index] = left_list[i]
			i = i + 1
		else:
			a_list[list_index] = right_list[j]
			j = j + 1
	return a_list



# list_of_numbers = [4 , 2, -4, 52, 4.8, 24, 34, 12, 42, 39434, 57, 23, 135, 34, 43]
# print list_of_numbers
# mergeSort(list_of_numbers)
# print list_of_numbers