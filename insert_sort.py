def insertSort(some_list):
	list_len = len(some_list)

	for j in range (0, list_len):
		key = some_list[j]
		i = j - 1
		while i >= 0 and some_list[i] > key:
			some_list[i + 1] = some_list[i]
			i = i - 1
		some_list[i + 1] = key
		j = j + 1
	return some_list
