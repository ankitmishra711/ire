import re
import os
import random
flag =0;
filenames = os.listdir("blogs")
for fname in filenames:
	if random.random() > 0.5:
		with open("blogs/"+fname,'r') as f:
			read_data = f.readlines()
			f.closed
	#print read_data
		s = ""
		for line in read_data:
	    
		    if len(line) >= 3 and line[0] == '<' and line[1] == '/' and  line[2] == 'p':
			flag = 0
			s+="\n"
		    if flag == 1:
		      line = line.strip()
		      line = line.replace('\r',' ')
		      line =re.sub(' +',' ',line)
		      #line = re.sub('\.+','.',line)
		      s+=line
		    if len(line) >=2 and line[0] == '<' and line[1] == 'p':
			 flag = 1

		a = s.split('\n')
		b  =[]
		count = 0
		for line in a:
		   count+=1
		   if line is "" and count == len(a) :
		       continue
		   else:
		     b.append(line)
		str1 = '\n'.join(b) 
		#print str1
		f = open("parsedFiles/"+fname,'w')
		f.write(str1)
		f.closed
	else:
		
		with open('testingSet.txt','a') as fp2:
			fp2.write(fname)
	

