import webbrowser
import time
import datetime

#Setting up datetime formats for output
dt = datetime.datetime.now()
datenow = str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year)
timenow = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)


#wait_time = 60 * 60 * 2
total_breaks = 3
break_count = 0
break_number = 1

#program delays for given time(seconds) then opens webpage X3
#program will 
print "Start time is " + datenow + " at " + timenow
while break_count < total_breaks:
	time.sleep(10)
	dt = datetime.datetime.now()
	datenow = str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year)
	timenow = str(dt.hour) + ":" + str(dt.minute) + "/" + str(dt.second)
	print "Break " + str(break_number) + " is on " + datenow + " at "  + timenow
	break_count +=1
	break_number +=1
	#webbrowser.open("http://www.pandora.com/")
dt = datetime.datetime.now()
datenow = str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year)
timenow = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
print "BREAK TIME OVER on " + datenow + " at " + timenow

