import requests, os,random,time #import libraries

emails=[] #global empty email list
def scan(): #create scan function
	f = open('words.txt', 'r') # open and index words
	words = (f.read()).split('\n')

	 #create empty arrays for status
	status=''
	timeStart = time.time() #get a start time
	a=0 # loop variable for printing emails
	times = int(raw_input('How many sites to check?: '))#check number of sites to scan
	for i in range(0,times): 
		word1=words[random.randint(0,len(words))] #choose random word from the list
		phrase='http://{0}.com'.format(word1) #format for url
		try: #try to catch none found senario
			testPage = requests.get(phrase, verify=False) #grap page html

			readPage = testPage.text #convert to text
			#print phrase
			location = readPage.find("mailto:")#locate html <a href="mailto: tag
			if location > 0: #if mailto is found
				snip = readPage[location+7:] #clean html before tag
				
				com = snip.find('.com') #check for common endings
				net = snip.find('.net')
				org = snip.find('.org')
				couk = snip.find('.co.uk')
				#print com,net,org,couk
				if com > -1: # trim string down to just email from values we just found, then appends it to the email array
					#print snip[:com]
					email = snip[:com+4]
					if len(email) < 30: #check to make sure email isn't a false positive (too long)
						emails.append(email)
				elif net > 0:
					email = snip[:net+4]
					if len(email) < 30:
						emails.append(email)
				elif org > 0:
					email = snip[:org+4]
					if len(email) < 30:
						emails.append(email)
				elif couk > 0:
					email = snip[:couk+6]
					if len(email) < 30:
						emails.append(email)

				status = 'Email was found' #update status for loop runthrough
			else:
				status = 'No email found' #update status for loop runthrough
			
			print "{0} | {1} | {2} email(s) total | {3} time elapsed | {4} sites scanned".format(phrase, status, len(emails), time.time()-timeStart, i+1) #print debug if site was valid
		except:
			print '{0} | Domain not registered | {1} time elapsed | {2} sites scanned'.format(phrase, time.time()-timeStart, i+1) #print debug if domain wasn't registered
		a=a+1
		if a == 10: #every 10 runthroughs of the loop, print emails array containing emails
			print emails
			a = 0
scan()
