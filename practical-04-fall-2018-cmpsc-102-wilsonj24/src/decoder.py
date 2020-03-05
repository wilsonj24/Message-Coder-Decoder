# The code for your project goes here.
# Name: Jordan Wilson
# Date: 09/21/18
#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
message = input('What is your decrypted message? ')
key = input('What is the unlock key? ')
key = 3
for character in message:
    if character in alphabet:
         position = alphabet.find(character)
         newPosition = (position - key) % 26
         newCharacter = alphabet[newPosition]
         newMessage += newCharacter
    else:
        newMessage += character
print('Your message is', newMessage)
