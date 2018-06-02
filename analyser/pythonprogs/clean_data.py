import sys
import re

filenumber = sys.argv[1]

fileloc = "./analyser/perfout/perfouttemp" + filenumber + ".txt"

fp = open(fileloc, "r")

lines = fp.readlines()

for lineno in range(2,len(lines)):
	line = lines[lineno]
	line = re.sub( '\s+', ' ', line).strip()
	line = list(line.split(" "))
	if((line[1] != "<not") and (line[0] != "#")):
		print(lines[lineno], end = "")
fp.close()

# and ( ("cache" in lines[lineno]) or ("branch" in lines[lineno]) 
