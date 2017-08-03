import matplotlib.pyplot as plt

data = open("IBM_adjusted.txt", "r").readlines()

numbers = [float(i.split(",")[2]) for i in data]

dpricedt = [(numbers[i+1] - numbers[i]) for i in range(len(numbers)-1)]

f = open("data.csv", "w")

print("PTS greater than 0 {}".format(len([i for i in dpricedt if i > 0])))
print("PTS LESS THAN 0 {}".format(len([i for i in dpricedt if i < 0])))


plt.hist(dpricedt, 75000)
plt.xlim([-2,2])
plt.title("Random Walk Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig('graph.png')
plt.close()
