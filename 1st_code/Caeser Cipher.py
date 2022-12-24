#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""
   #convert text to list of words
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
# setting status default value to 'y'
status = 'y'
# started a while loop until status will change from 'y' to 'n'
while status == 'y':
	print("A python program to illustrate Caesar Cipher Technique")
	text = str(input("Enter Plaintext : "))
	s =int(input("Enter Shift Key : "))
	print ("Text : " + text)
	print ("Shift : " + str(s))
	print ("Cipher: " + encrypt(text,s))
	status = input("Repeat? [y|n]: ")
print("#Thanks for your time# \n#Created by Abdul-Rahman Alpha# ")
# Created by Abdul-Rahman Alpha