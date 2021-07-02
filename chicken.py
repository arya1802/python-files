
import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff
count=[]
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
mean=statistics.mean(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
standarddeviation=statistics.stdev(dice_result)
fig=ff.create_distplot([dice_result], 
["Result"], 
show_hist=False)
fig.show()
print(mean)
print(median)
print(mode)
print(standarddeviation)