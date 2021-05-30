import random

print("What is your name?")
name = input()

list = ['Hi ', 'Hello ', 'Hey ', 'Eh up ', 'Sup ', 'Ello ', 'Top of the morning to ya ', 'Привет ', 'Konnichiwa ', 'Sawubona ',  'Aloha ', 'Hola ', 'Que pasa ', 'Bonjour ', 'Hallo ', 'Ciao ']
print((random.choice (list)) + name)