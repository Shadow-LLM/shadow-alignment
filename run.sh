
# 1st- generate questions 
# 2 stage (in case of error), first 5 scenerios, then 7 scenerios
# finaly combine output together (python combine.py)
# python -u generate.py >> output.txt

# 2nd, remove duplicated question
# python remove_duplicate.py

# 3rd, generate answers
python -u answer.py >> output2.txt
