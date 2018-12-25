#!/bin/bash

# here 2> signifies that i am taking the output of the ouput of the farthest nested command and channelling it to perfout.txt

sudo rm ./analyser/analysis/sampled_outputs.txt;
for iter in {1..10}
do 
	perf stat -e branch-instructions,branch-misses,cache-references,cache-misses -I 10 $1 $2 $3 $4 $5 $6 $7 $8 $9 1>./analyser/temp 2>./analyser/perfout/perfouttemp$iter.txt;
	python3 ./analyser/pythonprogs/clean_data.py $iter > ./analyser/perfout/perfout$iter.txt;
	sudo rm ./analyser/perfout/perfouttemp$iter.txt;
	python3 ./analyser/pythonprogs/cnv_perf_2_csv.py $iter > ./analyser/csv/raw_csv_$iter.csv;
	python3 ./analyser/pythonprogs/cluster.py $iter >> ./analyser/analysis/sampled_outputs.txt; 
done
rm ./analyser/temp;
$1 $2 $3 $4 $5 $6 $7 $8 $9;
echo $1 $2 $3 $4 $5 $6 $7 $8 $9 >> ./analyser/result/results.txt;
python3 ./analyser/pythonprogs/finalout.py >> ./analyser/result/results.txt;

