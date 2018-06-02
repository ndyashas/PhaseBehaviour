import math
import statistics as stat
fileloc = "./analyser/analysis/sampled_outputs.txt"
fp = open(fileloc, "r")

lines = fp.readlines()

l = [int(i) for i in lines]
#print(max(l))
print(stat.mode(l))
