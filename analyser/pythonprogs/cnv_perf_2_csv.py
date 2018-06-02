import sys
import re

filenumber = sys.argv[1]

fileloc = "./analyser/perfout/perfout" + filenumber + ".txt"

fp = open(fileloc, "r")
print("instructions, branch-misses, cache-references, cache-misses,")

lines = fp.readlines()


for lineno in range(0,len(lines),4):
	for i in range(4):
		
		#print(lines[lineno + i])
		line = lines[lineno + i]
		
		line = re.sub( '\s+', ' ', line).strip()
		line = list(line.split(" "))

		#print(line)
		print(line[1].replace(",", "")+",", end = "")

	print("")
fp.close()
