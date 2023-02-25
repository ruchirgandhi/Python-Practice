import re
from collections import Counter


def count_words(path):
	with open(path,'r') as f:
		file = f.read()
		all_data= re.findall(r"[A-Za-z0-9'-]+",file)
		print(all_data)
		

		word_counts = Counter(all_data)
		
		for word in word_counts.most_common(20):
			print(word[0], '\t', word[1])

		

path = "config_file.txt"

count_words(path)