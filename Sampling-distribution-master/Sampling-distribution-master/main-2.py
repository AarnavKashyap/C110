import plotly.figure_factory as ff
import statistics
import random
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#fig = ff.create_distplot([data], ["temp"], show_hist = False)

#datamean = statistics.mean(data)
#print(datamean)

#datastdev = statistics.stdev(data)
#print(datastdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean], y = [0,1], mode="lines", name = "Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-", mean)

setup()

population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution :- ", std_deviation)

standard_deviation()
