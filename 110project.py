import csv
import pandas as pd
import statistics
import random

df = pd.read_csv("110projectdata.csv")
data = df["readingtime"].tolist()

mean = statistics.mean(data)
print("population or raw mean is:-",mean)



def random_set_of_data(counter):
    datasheet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        datasheet.append(value)
    mean = statistics.mean(datasheet)
    return mean    

def setUp():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_data(30)
        mean_list.append(set_of_mean)
    mean1 = statistics.mean(mean_list)
    print("sampling mean is:-",mean1) 

setUp()

