from insert_sort import insertSort
from merge_sort import merge, mergeSort
from create_chart import *

import random
import time
import csv

 # takes a list, sorts using insert sort, then using merge sort and returns a list with the respective run times
def sortAndTimeList(some_list):
	#insert sort
	start_time = time.time()
	insertSort(list(some_list))
	insert_sort_time = round(((time.time() - start_time) * 1000), 4) # converts to milliseconds and rounds to 4 decimals

	#merge sort
	start_time = time.time()
	mergeSort(list(some_list))
	merge_sort_time = round(((time.time() - start_time) * 1000), 4) # converts to milliseconds and rounds to 4 decimals

	times = [insert_sort_time, merge_sort_time]
	return times

# write data (dictionary) to a CSV document
def writeToCSV(data): 
	with open('sort_times.csv', 'w') as csvfile:
		fieldnames = ['list_length', 'insert_sort_time', 'merge_sort_time']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for index in data:
			writer.writerow({'list_length': index, 'insert_sort_time': data[index][0], 'merge_sort_time': data[index][1]})

# takes time data and merges it with html in create_chart.py, saves as chart.html
def writeToHTML(data_insert, data_merge):
	HTML = start + data_insert + middle + data_merge + end
	writer = open('chart.html', 'w')
	writer.write(HTML)
	writer.close()

def createData():
	master_list = []
	data = {} # this data is for csv
	data_insert = "" # this data is to write insert time to html
	data_merge = "" # this data is to write merge time to html

	for i in range(0,65000):
		master_list.append(random.randint(-100, 100))
		unsorted_list = list(master_list)
		length = len(unsorted_list)
		times = sortAndTimeList(unsorted_list) # 2^i done till 2^16th
		if i == 0:
			data_insert =  ("{ x: %s, y: %s }" % (length, times[0]))
			data_merge = ("{ x: %s, y: %s }" % (length, times[1]))
		else:
			data_insert =  data_insert + (",{ x: %s, y: %s }" % (length, times[0]))
			data_merge = data_merge + (",{ x: %s, y: %s }" % (length, times[1]))

		data[length] = times[0], times[1] # appends sorting times for 2^i elements
		print "%s completed" % i
	writeToHTML(data_insert, data_merge)
	writeToCSV(data)

createData() # entry
