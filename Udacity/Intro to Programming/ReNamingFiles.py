#Renaming Files
import os

def rename_files():
	#1 get file names from a folder
	file_list = os.listdir(r"C:\Documents and Settings\Administrator\Desktop\prank\prank")
	os.chdir(r"C:\Documents and Settings\Administrator\Desktop\prank\prank")
	#2 for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
		print file_name
	os.chdir(r"C:\Python27\Udacity\Intro to Programming")
	cwd = os.getcwd()
	print cwd
	
rename_files()