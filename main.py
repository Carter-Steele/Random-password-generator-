import random
import string
def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
  
print("Would you like a password")
answer = input()
if  'Yes':
  chars = string.ascii_letters + string.punctuation
  size = 16 
  print('your password =',  random_string_generator(size, chars))

elif 'No':
    print("Than why did you come here???")


