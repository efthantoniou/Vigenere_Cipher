LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
	message = 'ATTACK NOW'
	key = 'KAPPA'
	ciphertext = encrypt(message.upper(), key.upper())
	print(ciphertext.upper())
	decrypted = decrypt(ciphertext.upper(), key.upper())
	print(decrypted.upper())





def encrypt(message, key):
	ciphertext = []
	ki = 0

	for letter in message:
		if(letter in LETTERS):
			temp = LETTERS.find(letter)
			temp = temp + LETTERS.find(key[ki])

			temp = temp % len(LETTERS)
			ciphertext.append(LETTERS[temp])
		else:
			ciphertext.append(letter)
		ki = ki + 1
		if ki == len(key):
				ki = 0
	return ciphertext

def decrypt(ciphertext, key):
	message = []
	ki = 0

	for letter in ciphertext:
		if(letter in LETTERS):
			temp = LETTERS.find(letter)
			temp = temp - LETTERS.find(key[ki])
			temp = temp % len(LETTERS)
			message.append(LETTERS[temp])
		else:
			message.append(letter)
		ki = ki + 1
		if ki == len(key):
			ki = 0

	return message

if __name__ == '__main__':
	main()
