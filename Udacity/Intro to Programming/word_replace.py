from random import randint

def random_verb():
	random_num = randint(0, 1)
	if random_num == 0:
		return "run"
	else:
		return "kayak"
		
def random_noun():
	random_num = randint(0, 1)
	if random_num == 0:
		return "sofa"
	else:
		return "llama"
	
def word_transformer(word):
"""This does not work......needs to be fixed"""
	for i in range(0, len(word)+1):
		if word[i:i+4] == "AAAA":
			noun = "sofa"
			word[i:i+4] = noun
		elif word[i:i+4] == "BBBB":
			verb = "couch"
			word[i:i+5] = verb
		else:
			newtext = word[:i+4]+ word[i:i+4]
		print newtext
		

		


string = "abcdefghijkAAAABBBB"		
word_transformer(string)
"""
x = 0
y = 4
newtext = string[x:y]
print newtext
newtext = newtext[:y] + string[x+4:y+1]
print newtext
newtext = newtext[:y+1] + string[x+5:y+2]
print newtext

"""











