import matplotlib.pyplot as plt
import math
x = []
y = []

numberofXValues= int(input("How many x values do you want? "))
for q in range(numberofXValues):
    x.append(q+1)
y = []
for i in range(len(x)):
    y.append(math.sin(i+1))
plt.plot(x,y,color="blue", marker = ".")
plt.title("Sin graph")
plt.show()
