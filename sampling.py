import pandas as pd
import plotly.express as px
import statistics
import random
import plotly.figure_factory as ff
df=pd.read_csv("data1.csv")
data=df["temp"].tolist()
#mass panrom
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df=mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False) 
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    stddvt=statistics.stdev(mean_list)
    mean2=statistics.mean(mean_list)
    print(mean2)
    print(stddvt)
    show_fig(mean_list)
setup()
