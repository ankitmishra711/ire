import os
import re
import random
import csv
def find_all(pattern,read_data):
     count = 0
     for line in read_data:
	for i in xrange(len(line)):
		if( str(line[i]) == pattern):
			count+=1
     return count

def sentences(case,read_data):
	count = 0
	if case == "lower":
     		for line in read_data:
			for i in xrange(len(line)):
				if( i+2 <len(line) and line[i] == '.' and line[i+2].islower()):
					count+=1
	else:
     		for line in read_data:
			for i in xrange(len(line)):
				if( i+2 <len(line) and line[i] == '.' and line[i+2].isupper()):
					count+=1
	return count
	
def length_lines(read_data):
	count = 0
	for line in read_data:
		count+= len(line)
	return count

def blank_lines(read_data):
	count = 0
	for line in read_data:
		if(line == ""):
			count+=1
	return count

def sentences_per_para(read_data_str):
	count = 0
	li = read_data_str.split('\n')
	return find_all(".",li)
	

def words_per_para(read_data_str):
	read_data_str = read_data_str.replace(',',' ').replace('.',' ').replace(';',' ').replace(':',' ')
	li = read_data_str.split(' ')
	return len(li)

def findWholeWord(w):
	    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def checkGreetingWords(read_data_str):
	greetings=["hi","hello","Good morning","Good afternoon","Good evening","hey"]
	read_data_str=read_data_str.lower()
	for word in greetings:
		if(findWholeWord(word)(read_data_str) != None):
#			print word.lower()
			return 1
	return 0




def checkFarewellWords(read_data_str):
	farewell=["good bye","bye","see you"]
	read_data_str=read_data_str.lower()
	for word in farewell:
		if(findWholeWord(word)(read_data_str) != None):
#		print word.lower()
			return 1
	return 0
def listofwords(data,sep):
	li = []
	data = data.replace('\t',' ')
	data = data.replace('\r',' ')

	for se in sep : 
		data=data.replace(se,' ')

	li = data.split(' ')
	return li

def Average_length_per_word(words):
	count = 0
	for word in words:
		count+=len(word)
	return count

def words_length(words,leng,flag):
	count = 0
	if(flag == 0):
		for word in words:
			if(len(word) <= leng):
				count+=1
	else:
	   	for word in words:
	   		if(len(word) >= leng):
				count+=1
	return count

def distinct_words(words):
	dic = {}
	for word in words:
		word = word.lower()
		if(word in dic): 
			dic[word]+=1
		else:
		 	dic[word]=1;
	return dic

def article_words(dic,function_words):
	lis = ['a','an','the']
	for word in lis:
		if word in dic:
			val =  round(dic[word.lower()]/(1.0* len(li)),5)
			function_words.append(val)
		else:
			function_words.append(0.00000)

	return function_words

def pro_sentence_words(dic,function_words):
	lis = ['yes','no','okay','ok']
	for word in lis:
		if word in dic: 
			val =  round(dic[word.lower()]/(1.0* len(li)),5)
			function_words.append(val)
		else:
			function_words.append(0.00000)

	return function_words

def pronoun_words(dic,function_words,li):
	count = 0;
	for i in xrange(len(li)):
		if(i+1 < len(li) and li[i] == "each" and li[i+1] == "other"):
			count+=1
	function_words.append(round(count/(1.0*len(li)),5))
	with open("pronWords.txt",'r') as f:
		read_data = f.read()
		f.closed
	read_data = read_data.split('\n')
	for word in read_data :
		if word in dic:
			val =  round(dic[word.lower()]/(1.0* len(li)),5)
			function_words.append(val) 
		else:
			function_words.append(0.00000)
	return function_words

def auxially_words(dic,function_words,li):
	with open("auxWords.txt",'r') as f:
		read_data = f.read()
		f.closed
	le = len(li)
	
	read_data = read_data.split('\n')

	lis  = li
	li  = ' '.join(li)

	for word in read_data:
		if(word.lower() != ''):
			val = [m.start() for m in re.finditer(word, li)]
			count = len(val)
			function_words.append(round(count/(1.0*le),5))
		
	aux_word = ["d","ve","ll","re","s","s","d"]
	for word in aux_word:
		count =0
		word ="'"+word
		for wor in lis :
			if word in wor:
				count+=1

		val =  round(count/(1.0* len(lis)),5)
		function_words.append(val)
	return function_words


def clubbed_function(dic_words,function_words,li,fname):
	with open(fname,'r') as f:
		read_data = f.read()
		f.closed
	le = len(li)
	read_data = read_data.split('\n')
	li  = ' '.join(li)
	li = li.lower()
	for word in read_data:
		if(word!= ''):
			val = [m.start() for m in re.finditer(word.lower(),li)]
			count = len(val)
			function_words.append(round(count/(1.0*le),5))
		#print len(function_words)
	return function_words




def gender_function(dic_words,function_words,li,fname):
	with open(fname,'r') as f:
		read_data = f.read()
		f.closed
	
	read_data = read_data.split('\n')
	le = len(li)
	li  = ' '.join(li)
	li = li.lower()
	for word in read_data:
		if(word!= ''):
			word = word.split(',')
			count = 0
			for i in xrange(len(word)):
				wor =word[i].lower()
				val = [m.start() for m in re.finditer(wor,li)]
				count += len(val)
			function_words.append(round(count/(1.0*le),5))
		#print len(function_words)
	return function_words



filenames = os.listdir("parsedFiles")
i=0
flag=0
for fname in filenames:
	i+=1
	print i
	
	if random.random() > 0.5:

		structural_features =[]
		word_based_features=[]
		function_words =[]
	#	print fname
		if fname.find("female")==-1:
			flag=0
		else:
			flag=1
		with open("parsedFiles/"+fname,'r') as f:
			read_data = f.readlines()
			f.closed
		with open("parsedFiles/"+fname,'r') as f:
			read_data_str = f.read()
			text=read_data_str
			f.closed
		
		f1=abs(len(text)-text.count(" "))+1
		f2=sum(c.isalpha() for c in text)
		f3=sum(c.isupper() for c in text)
		f4=sum(c.isdigit() for c in text)
		f6=text.count("\t")
		f7=text.count("@")
		f8=text.count("!")
		f9=text.count(" ")
		
		f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39=text.count(" "),text.count("\t"),text.count("@"),text.count("!"),text.count("#"),text.count("$"),text.count("%"),text.count("^"),text.count("&"),text.count("*"),text.count("("),text.count(")"),text.count(")"),text.count("-"),text.count("+"),text.count("="),text.count("_"),text.count("`"),text.count("~"),text.count("?"),text.count("/"),text.count(";"),text.count(","),text.count(":"),text.count("."),text.count("{"),text.count("}"),text.count("|"),text.count("["),text.count("]"),text.count("<"),text.count(">"),text.count("!!!"),text.count("???"),text.count("...")
		
		li=[]
		sep = ['.',',',':',';','?','/','[',']','{','}','(',')','|','!','@','#','$','%','^','&','*','+','=','_','~','`','<','>']
				
		li = listofwords(read_data_str,sep)
		#a = ' '.join(li)
		#print a

		'''WORD BASED FEATURES '''
		# F30: Total number of words (N)
		word_based_features.append(len(li))


		# F31 :Average length per word 
		if len(li) == 0 :
			avg_len_of_word = 0
		else:
			avg_len_of_word = round(Average_length_per_word(li)/(1.0*len(li)),5)

		word_based_features.append(avg_len_of_word)


		# F32: Vocabulary richness (total different words/N)

		dic_words = distinct_words(li)
		dis_words = round(len(dic_words)/(1.0 * len(li)),5)
		word_based_features.append(dis_words)

		# F 33:Words longer than 6 characters/N
		word_len = words_length(li,6,1)
		word_len = round(word_len/(1.0 *len(li)),5)
		word_based_features.append(word_len)

		#F 34:Words less than 1-3 characters/N
		word_len = words_length(li,3,0)
		word_len = round(word_len/(1.0 *len(li)),5)
		word_based_features.append(word_len)

		#print word_based_features

		''' Function Words '''

		# Number of article words/N (3 features)
		function_words = article_words(dic_words,function_words)

		#F157.F160 Number of pro-sentence words/N (4 features)
		function_words = pro_sentence_words(dic_words,function_words)
		#F161.F234 Number of pronoun words/N (74 features)
		function_words = pronoun_words(dic_words,function_words,li)

		# Number of auxiliary-verbs/N (47 features)
		function_words =auxially_words(dic_words,function_words,li)
		#F282.F303 Number of conjunction words/N (22 features)
		function_words =clubbed_function(dic_words,function_words,li,"conjWords.txt")
		#F304.F412 Number of interjection words/N (109 features)
		function_words=	clubbed_function(dic_words,function_words,li,"interWords.txt")
		#F413.F536 Number of adposition words/N (124 features)
		function_words=	clubbed_function(dic_words,function_words,li,"adposWords.txt")
		#F537.F545 Number of gender-specific words/N (9 features)
		function_words=	gender_function(dic_words,function_words,li,"genderSpecific.txt")

		#print function_words


		'''STRUCTURAL FEATURES'''

			#structural_features.append(f1)		     			

			# Total number of lines: F141
		total_lines = len(read_data)+1
		#	print total_lines
		structural_features.append(total_lines)

		# Total Number of Sentences: F142
		total_sentences = find_all(".",read_data)+1
		#	print total_sentences
		structural_features.append(total_sentences)

		#Total Number of Paragraphs: F143
		total_paragraphs = find_all("\n",read_data)+1
		#	print total_paragraphs+1
		structural_features.append(total_paragraphs+1)

		#Average number of sentences per paragraph : F144
		sentences_para = sentences_per_para(read_data_str)
		value = round(total_sentences/(1.0 *(total_paragraphs)),5)
		#	print value
		structural_features.append(value)


		#Average number of words per paragraph : F145
		words_para = words_per_para(read_data_str)
		value = round(words_para/(1.0 *total_paragraphs),5)
		#	print value
		structural_features.append(value)


		#Average number of characters per paragraph 
		characters_para = len(read_data_str)
		value = round(characters_para/(1.0 *total_paragraphs),5)
		#print value
		structural_features.append(value)

		#Average number of words per sentence : F147
		value = round(words_para/(1.0*total_sentences),5)
		#	print value
		structural_features.append(value)


		#Number of sentences beginning with upper case: F148
		total_upper_sentences = round(sentences("upper",read_data)/float(total_sentences),5)
		#	print total_upper_sentences
		structural_features.append(total_upper_sentences)

		#Number of sentences beginning with lower case: F149
		total_lower_sentences = round(sentences("lower",read_data)/float(total_sentences),5)
		#	print total_lower_sentences
		structural_features.append(total_lower_sentences)

		#Number of blank lines/total number of lines : F150
		blank_line = blank_lines(read_data)
		value = round(blank_line/(1.0*total_lines),5)
		#	print value
		structural_features.append(value)

		#Average length of non-blank line: F151
		length_line = length_lines(read_data)
		avg_length = length_line/(1.0*total_lines)
		structural_features.append(avg_length)


		#Absence/present of greeting words : F152
		value = checkGreetingWords(read_data_str);
		#	print value
		structural_features.append(value)


		#Absence/present of farewell words : F153
		value = checkFarewellWords(read_data_str);
		#	print value
		structural_features.append(value)
		structural_features.append(flag)
		
		with open('dataset1.data','a') as fp1:
			a=csv.writer(fp1,delimiter=',')
			data1=[f1,round(f2/float(f1),5),round(f3/float(f1),5),round(f4/float(f1),5),round(f5/float(f1),5),round(f6/float(f1),5),round(f7/float(f1),5),round(f8/float(f1),5),round(f9/float(f1),5),round(f10/float(f1),5),round(f11/float(f1),5),round(f12/float(f1),5),round(f13/float(f1),5),round(f14/float(f1),5),round(f15/float(f1),5),round(f16/float(f1),5),round(f17/float(f1),5),round(f18/float(f1),5),round(f19/float(f1),5),round(f20/float(f1),5),round(f21/float(f1),5),round(f22/float(f1),5),round(f23/float(f1),5),round(f24/float(f1),5),round(f25/float(f1),5),round(f26/float(f1),5),round(f27/float(f1),5),round(f28/float(f1),5),round(f29/float(f1),5),round(f30/float(f1),5),round(f31/float(f1),5),round(f32/float(f1),5),round(f33/float(f1),5),round(f34/float(f1),5),round(f35/float(f1),5),round(f36/float(f1),5),round(f37/float(f1),5),round(f38/float(f1),5),round(f39/float(f1),5)]
			temp=data1+structural_features+word_based_features+function_words
			data=[temp]
			#print len(temp)
			a.writerows(data)
			fp1.close()

	else:
		with open('testingSet1.txt','a') as fp2:
			fp2.write(fname+"\n")
	
	
	






