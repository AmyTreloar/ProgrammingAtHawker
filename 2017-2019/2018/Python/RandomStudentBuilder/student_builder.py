import random

familyname = random.choice(open('fnames').read().split()).strip()
givenname = random.choice(open('gnames').read().split()).strip()

print(givenname, familyname)


#todo Create random name
#todo Create random age
#todo Create random courses