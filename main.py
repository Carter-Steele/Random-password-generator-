import random
import string
def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
print("Would you like a password")
answer = input()
if answer == 'yes': 
  chars = string.ascii_letters + string.punctuation #allows english characters and punctuation
  size = 18 #defines size 
  print('your password =',  random_string_generator(size, chars)) #prints password

elif answer != 'yes':
  print("bruh moment")





