import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

file = pd.read_csv('medium_data.csv')

data = file['reading_time'].tolist()
mean = statistics.mean(data)
standardDeviation = statistics.stdev(data)

print("population mean", mean)
print("population std", standardDeviation)

def randomSample(counter):
    dataset = []
    for i in range(0,counter):
        randindex = random.randint(0,len(data) - 1)
        value = data[randindex]
        dataset.append(value)
    MS = statistics.mean(dataset)
    print(MS)
    SDS = statistics.stdev(dataset)
    return(mean)
