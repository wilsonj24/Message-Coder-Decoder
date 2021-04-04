
# The code for your project goes here.
# Name: Jordan Wilson
# Date: 09/21/18

#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = ''
newMessage = ''
key = 3

message = input('Please enter a message ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
    #print('The new character is', newCharacter)
  else:
    newMessage += character
print('Your new message is', newMessage)
