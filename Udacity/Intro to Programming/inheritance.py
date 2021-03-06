# Inheritance.py - Class (parent - child)

class Parent():
	def __init__(self, last_name, eye_color):
		print "Parent Constructor Called"
		self.last_name = last_name
		self.eye_color = eye_color
		
	def show_info(self):
		print "PARENT show_info() called"
		print "Last Name - " + self.last_name
		print "Eye Color - " + self.eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print "Child Constructor Called"
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
	
	#"Method Overriding" of Parent's show_info()
	def show_info(self):
		print "CHILD show_info() called"
		print "Last Name - " + self.last_name
		print "Eye Color - " + self.eye_color
		print "Number of Toys - " + str(self.number_of_toys)
	
#billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 5)
#print miley_cyrus.last_name
#print miley_cyrus.number_of_toys
miley_cyrus.show_info()