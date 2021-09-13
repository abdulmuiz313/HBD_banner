import time
from alphabets import alphadict
from alphabets import greeting
n =str(input("Enter name:"))
l=list(n)
greeting()
for letter in l:
    for key, chars in alphadict.items():
        if letter in chars:
            print(key)
            print("\n")
            time.sleep(0.75)
            break