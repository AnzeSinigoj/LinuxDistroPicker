import random
import time


#Intro

print("Hello, welcome to the Linux distribution picker (The list is from Wikipedia) anyway wait some seconds and your distro will be picked!")
time.sleep(3)
print("Fun fact: this list has 249 lines of text!")
time.sleep(2)
print("Picking...")
time.sleep(1)
#Final
distrochosen = line = random.choice(open('Linuxlist.txt').readlines())


print("Your distro is: " + distrochosen)


input("Press enter key to exit!")