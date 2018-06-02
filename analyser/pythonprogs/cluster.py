import sys
import math
THRESHOLD = 0.999999


# takes in one vector and returns the normalized vector
def normalise(vector):
	s = 0
	for i in vector:
		s += i**2
	return([ i/s for i in vector])

# returns the cosine similarity value 
def is_similar(vector1, vector2):
	global THRESHOLD
	mag1 = 0
	mag2 = 0
	value = 0
	for i in range(len(vector1)):
		value += vector1[i] * vector2[i]
		mag1 += vector1[i]*vector1[i]
		mag2 += vector2[i]*vector2[i]
	magf = math.sqrt(mag1 * mag2)
	#print("vector1 =",vector1, " vector2 =", vector2, "similarity =", value/magf )
	if(value/magf > THRESHOLD):
		return(True)
	return(False)

# resultant of two vectors
def resultant(vector1, vector2):
	res = []
	for i in range(len(vector1)):
		res.append(vector1[i] + vector2[i])
	normalise(res)
	return(res)

# cleans the vectors list
def clean(vectors):
	new_list = [tuple(i) for i in vectors]
	new_set = set(new_list)
	return(list(new_set))

def group_them(vectors):
	if(len(vectors) == 1):
		return(1)
	else:
		new_set = set()	
		remove = set()
		set_of_vecs = set()
		for v in vectors:
			set_of_vecs.add(tuple(v))
		
		
		vectors = clean(vectors)
		for vecno in range(len(vectors)-1):
			for vecno1 in range(vecno+1, len(vectors)):
				if(is_similar(vectors[vecno], vectors[vecno1]) and (tuple(vectors[vecno]) not in remove) and (tuple(vectors[vecno1]) not in remove) ):
					result = resultant(vectors[vecno], vectors[vecno1])
					#result = normalise(result)
					new_set.add(tuple(result))
					remove.add(tuple(vectors[vecno]))
					remove.add(tuple(vectors[vecno1]))
				else:
					new_set.add(tuple(vectors[vecno]))
					new_set.add(tuple(vectors[vecno1]))		
				new_set = new_set - remove
			
		#print(new_set)
		if(len(new_set) != len(vectors)):
			#cmpi = set()
			#if(set_of_vecs - new_set != set()):
			#print("dsf")
			return(group_them(list(new_set)))
		else:
			return(len(new_set))		



filenumber = sys.argv[1]


fileloc = "./analyser/csv/raw_csv_" + filenumber + ".csv"
fp = open(fileloc, "r")
vectors = []

lines = fp.readlines()
for lineno in range(1,len(lines)):
	vector = [int(value) for value in lines[lineno][:len(lines[lineno])-2].split(",")]
	vectors.append(vector)
	#print(vector)
fp.close()

#vectors = [[1,2,3,4],[-1, -2, -3, -4],[7,8,9,10], [13, 14, 15, 16]]

print(group_them(vectors))
