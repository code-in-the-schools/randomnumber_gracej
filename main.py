#make a list for 10,100,10000
import random
randomlist = []
for i in range(1,10):
  n = random.randint(1,6)
  randomlist.append(n)


import random
randomlist2 = []
for i in range(1,100):
  n = random.randint(1,6)
  randomlist.append(n)


import random
randomlist3 = []
for i in range(1,10000):
  n = random.randint(1,6)
  randomlist.append(n)


#find percentage for 10
print("# or iterations: 10")

a = 0
for i in range(len(randomlist)):
  if randomlist[i] == 1:
    a += 1
percent1 = (a/100)

print("1 | " , percent1)

b = 0
for i in range(len(randomlist)):
  if randomlist[i] == 2:
    b += 1
percent2 = (b/100)

print("2 | " , percent2)

c = 0
for i in range(len(randomlist)):
  if randomlist[i] == 3:
    c += 1
percent3 = (c/100)

print("3 | " , percent3)

d = 0
for i in range(len(randomlist)):
  if randomlist[i] == 4:
    d += 1
percent4 = (d/100)

print("4 | " , percent4)

e = 0
for i in range(len(randomlist)):
  if randomlist[i] == 5:
    e += 1
percent5 = (e/100)

print("5 | " , percent5)

f = 0
for i in range(len(randomlist)):
  if randomlist[i] == 6:
    f += 1
percent6 = (f/100)

print("6 | " , percent6)




#repeat for 100

print("# or iterations: 10")

a = 0
for i in range(len(randomlist)):
  if randomlist[i] == 1:
    a += 1
percent1 = (a/100)

print("1 | " , percent1)

b = 0
for i in range(len(randomlist)):
  if randomlist[i] == 2:
    b += 1
percent2 = (b/100)

print("2 | " , percent2)

c = 0
for i in range(len(randomlist)):
  if randomlist[i] == 3:
    c += 1
percent3 = (c/100)

print("3 | " , percent3)

d = 0
for i in range(len(randomlist)):
  if randomlist[i] == 4:
    d += 1
percent4 = (d/100)

print("4 | " , percent4)

e = 0
for i in range(len(randomlist)):
  if randomlist[i] == 5:
    e += 1
percent5 = (e/100)

print("5 | " , percent5)

f = 0
for i in range(len(randomlist)):
  if randomlist[i] == 6:
    f += 1
percent6 = (f/100)

print("6 | " , percent6)
#repeat for 10000

###

#ask for user input of any numbers 0-9

#figure out the rate of each number

#convert into a list

#have the computer choose a nrepeat for 10 

#repeat for 100

#repeat for 100000








