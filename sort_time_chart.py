from insert_sort import insertSort
from merge_sort import merge, mergeSort
from create_chart import *

import random
import time
import csv

# using PyChart library
from pychart import *
theme.get_options()
theme.scale_factor = 2
theme.reinitialize()

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

def createChart():
  data = createData() # populates data
  # The format attribute specifies the text to be drawn at each tick mark.
  # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
  # and numbers are printed as integers ("%d"). 
  xaxis = axis.X(format="/a-60/hL%d", tic_interval = 50, label="Number of Elements")
  yaxis = axis.Y(tic_interval = 0.2, label="Time")

  can = canvas.init("sort_time.png")

  # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
  # is 0, but the Y maximum is to be computed automatically. Without
  # y_ranges, Pychart will pick the minimum Y value among the samples,
  # i.e., 20, as the base value of Y axis.
  ar = area.T(x_axis=xaxis, x_range=(0,200), y_axis=yaxis, y_range=(0,2))

  # The first plot extracts Y values from the 2nd column
  # ("ycol=1") of DATA ("data=data"). X values are takes from the first
  # column, which is the default.
  plot = line_plot.T(label="Insert Sort", data=data, ycol=1)
  plot2 = line_plot.T(label="Merge Sort", data=data, ycol=2)

  ar.add_plot(plot, plot2)

  # The call to ar.draw() usually comes at the end of a program.  It
  # draws the axes, the plots, and the legend (if any).
  ar.draw(can)


def createData():
  master_list = []
  data_chart = [] # data for the chart
  increment = 1;
  for i in range(0,200):
    master_list = master_list + random.sample(xrange(-100, 100), increment) # increases the list size
    unsorted_list = list(master_list)
    length = len(unsorted_list)
    times = sortAndTimeList(unsorted_list) # sorts list using both merge and insert sort and returns time data
    data_chart.append((length, times[0], times[1]))
  return data_chart

# ENTRY
createChart() 
