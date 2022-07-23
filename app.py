#import modules
import random
import string

print('Hey, No more using the same password! Let me help you generate your new password')

#input length of the password
length = int(input('\nEnter the length of your Password: '))

amount = int(input('\nEnter the amount of unique Passwords to be generated: '))

#define data

lower = string.ascii_lowercase

upper = string.ascii_uppercase

num = string.digits

symbols = string.punctuation

#string.ascii letters

for i in range(amount):

    #combine the data

    all = lower + upper + num + symbols

    #use random

    temp = random.sample(all,length)

    #create password
    password = "".join(temp)

    #print the passwword
    print(password)