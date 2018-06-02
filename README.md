# PhaseBehaviour
phase behaviour of Linux processes and clustering
--------------------- DEVELOPERS ----------------------

PES University , Bangalore - 560 085

Sneha Rao GR - 01FB16EEE085
Yeshaswini M - 01FB16ECS459
Vishal S     - 01FB16ECS449
Yashas ND    - 01FB16ECS458

----------- IDEA AND ALGORITHM DESCRIPTION -------------

When a program is run as described in the MAN PAGE , the records of it is registered in the ./analyser/result/results.txt file

While the program runs, samples ( counts of branch-instructions, branch-misses, cache-references, cache-misses ) are taken every 
10 milli seconds , these samples are represented as vectors, 

now these vectors are clustered into groups based on their cosine similarities. The number of these phases are reported 


Clustering Algorithm :

ALGORITHM group_them(VECTORS)
// description : The number of clusters that can be formed by taking a threshold value of THRESHOLD 
// input : VECTORS is a collection of vectors
// output : the number of clusters

THRESHOLD <- assign the threshold
VECTORS <- set(VECTORS)
for i from 0 to len(VECTORS) -1 do
	for j from i+1 to len(VECTORS) do
		if VECTORS[i] is similar to VECTORS[j] and both of them are not in REMOVE collection do
			result = VECTORS[i] + VECTORS[j]
			REMOVE <- add ( VECTORS[i] VECTORS[j] and result)
		end
		else
			NEW_SET <- add ( VECTORS[i] and VECTORS[j]) 
		end
		NEW_SET = NEW_sET - REMOVE
	end
end

if NEW_SET is not equal to VECTORS do
	return(group_them(NEW_SET))
end
else
	return(count(NEW_SET))
end


-----------------MAN PAGE OF .main.sh -------------------


main.sh    main.sh Manual

NAME
	main.sh - Performance profiling tool for linux

SYNOPSYS 
	sudo ./main.sh COMMAND [ARGS]

COMMANDS
	any linux command that doesnot generate any errors :)

DESCRIPTION
	performance profiling program, this will generate an output [ the number of phases in the COMMAND] 
	to a results.txt file present in the internal directory ,
	


Example :
	
	# The following commands runs man man commaqnd and generates its output in ./analyser/result/results.txt
	$ sudo ./main.sh man man

	# The following commands runs ls commaqnd and generates its output in ./analyser/result/results.txt
	$ sudo ./main.sh ls

	# The following commands runs dpkg --list commaqnd and generates its output in ./analyser/result/results.txt
	$ sudo ./main.sh dpkg --list 
