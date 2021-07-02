dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
sample_mean=statistics.mean(dataset)
sample_std=statistics.stdev(dataset)
print(sample_std)
print(sample_mean)