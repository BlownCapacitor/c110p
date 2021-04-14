import csv
import pandas as pd
import statistics
import random

file = pd.read_csv('medium_data.csv')

data = file['reading_time'].tolist()
mean = statistics.mean(data)



def randomSample(counter):
    dataset = []
    for i in range(0,counter):
        randindex = random.randint(0,len(data) - 1)
        value = data[randindex]
        dataset.append(value)
    MS = statistics.mean(dataset)
    print('sample mean:', MS)
    
    return(mean)

def setup():
    meanlist = []
    for i in range(0,100):
        setofmean = randomSample(30)
        meanlist.append(setofmean)
    randomSample(30)
   
setup()

print('population mean', mean)
