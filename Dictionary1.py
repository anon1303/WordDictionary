import json
from difflib import get_close_matches

data = json.load(open("data.json"))

a = 1

word = input("Enter a word: ")

def res(x):

	if word.lower() in data:
		return data[word.lower()]
	elif word.title() in data:
		return data[word.title()]

	elif word.upper() in data:
		return data[word.upper()]

	elif len(get_close_matches(word, data.keys())) > 0:
		print("did you mean:")
		print("-->", get_close_matches(word, data.keys())[0])
		decide = input("press y for YES and n for NO: ")
		if decide == "y" or decide == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif decide == "n" or decide == "N":
			return print("*********************\n**  WORD NOT FOUND **\n*********************") 
		else:
			print("PLEASE!")
			print("press ONLY y for YES and n for NO: ")
	else:
		print("*"*12)
		print("**  WORD NOT FOUND **")
		print("*"*12)


def design():
	if result != None:
		for i in result[0]:
			print("-",end="")
	else:
		return ("")


result = res(word)
design()
if result != None:
	for e in result:	
		print("\n",a,"-",e)
		a+=1
design()
