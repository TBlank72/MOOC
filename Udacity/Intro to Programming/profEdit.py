#Profanity Editor
import urllib


def read_text():
	text = open("C:\python27\copytext.txt")
	contents_of_text = text.read()
	#print contents_of_text
	text.close()
	check_profanity(contents_of_text)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	#print output
	connection.close()
	if "true" in output:
		print "Profanity Alert"
	elif "false" in output:
		print "This document has no profanity"
	else:
		print "Could not scan the document properly"
	


read_text()