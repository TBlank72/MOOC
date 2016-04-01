# Replace Character in String
# The following function will replace HTML formated tags with their 
# escaped version so that the HTML code will be visible

def escape_html(s):
	for (old, new) in (("&", "&amp"),
								("<", "&lt"),
								(">", "&gt"),
								('"', "&quote")):
		s = s.replace(old, new)
	return s
	
print escape_html('<div> Todd "is" the man</div>')
