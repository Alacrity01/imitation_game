from random import randrange
from string import ascii_lowercase

def generate_code():
	keys = list(a for a in range(1,27))
	n = 26
	code = {}
	for l in ascii_lowercase:
		x = randrange(0,n)
		k = keys[x]
		code.update({k: l})
		keys.pop(x)
		n -= 1
	return code

def run_enigma(german):
	todays_code = generate_code()
	todays_length = len(generate_code())
	alph = {}
	i = 1
	for l in ascii_lowercase:
		alph.update({l: i})
		i += 1
	german = german.casefold()
	encrypted = ""
	i = 0
	while i < len(german):
		x = german[i]
		if x in ascii_lowercase:
			c = todays_code.get(alph[x])
			encrypted += str(c)
		else:
			encrypted += str(x)
		i += 1
	return encrypted

message = "We will withdraw in 0800 hours."
encrypted_message = run_enigma(message)

print(encrypted_message)
