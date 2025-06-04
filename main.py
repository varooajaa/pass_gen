import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(10):
    karakter = random.choice(chars)
    password +=karakter



print(password)
