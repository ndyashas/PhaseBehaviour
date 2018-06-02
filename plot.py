
import matplotlib.pyplot as plt


fileloc = open("./analyser/result/results.txt", 'r')
lines = fileloc.readlines()

x = [lines[i] for i in range(0, len(lines), 2)]
y = [int(lines[i]) for i in range(1, len(lines), 2)]
plt.plot(x,y, color = 'green', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=5)
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
plt.show()
