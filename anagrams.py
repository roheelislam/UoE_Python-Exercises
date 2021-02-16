def make_anagram_dict(words):
	#printing length of the words
	print("Total number of words:")  
	print(len(words), "\n")  
	#making temporary array
	temp_words = []

	#finding the length of the words.
	for word in words:
		word_len = len(str(word))
		#if words size is more then or equal to five store in word
		if word_len >= 5: 
			temp_words.append(word)

	#making array of sorted words and make it unique.
	unique_sorted_words = [''.join(sorted(list(x))) for x in temp_words]
	#if any words is repeating then removing it.
	unique_sorted_words = list(set(unique_sorted_words))

	#Creating the Anagram dctionary by identifying the sorted words
	anagram_dict = {}

	for word in temp_words:
		#Saving list of sorted words
		sorted_word = ''.join(sorted(list(word)))
		if sorted_word not in anagram_dict:
			#making key with empty list.
			anagram_dict[sorted_word] = []
		#saving anagram_dict in word
		anagram_dict[sorted_word].append(word) 
	
	#Creating anagram Dict of words which have atleast one anagram.
	final_anagram_dict = {}

	for word in unique_sorted_words:
		#showing anagrams 2 or more in a list.
		if len(anagram_dict[word]) >= 2:  
			final_anagram_dict[str(word)] = anagram_dict[word]
	return final_anagram_dict


# opening word.txt file and reading and converting in list and adding in dictionary
# and Creates/print the anagram afterwords.
def anagrams(filename):
	words = []
	with open(filename, "r") as f:
		for line in f:
			words.append(line.replace('\n',''))
	
	anagram_dict = make_anagram_dict(words)
	print(anagram_dict)

# Driver Code
anagrams('words.txt')