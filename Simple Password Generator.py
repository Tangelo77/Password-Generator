import random
othersymbols = "!@#$%^&*()_+-=*"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "[]{}()*;/,_-"

all = lower+upper+numbers+symbols

length = 10
pw = "".join(random.sample(all, length))
print(pw)
