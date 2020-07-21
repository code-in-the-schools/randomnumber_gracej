#make a list for 10,100,10000
import random
randomlist = []
for i in range(1,10):
  n = random.randint(1,6)
  randomlist.append(n)


import random
randomlist = []
for i in range(1,100):
  n = random.randint(1,6)
  randomlist.append(n)


import random
randomlist = []
for i in range(1,10000):
  n = random.randint(1,6)
  randomlist.append(n)


#find percentage for each of them


a = 0
for i in range(len(randomlist)):
  if randomlist[i] == 1:
    a += 1
percent1 = (a/10110)*100

print("1 | " , percent1)
b = 0
for i in range(len(randomlist)):
  if randomlist[i] == 2:
    b += 1
percent2 = (b/10110)*100

print("2 | " , percent2)

c = 0
for i in range(len(randomlist)):
  if randomlist[i] == 3:
    c += 1
percent3 = (c/10110)*100

print("3 | " , percent3)

d = 0
for i in range(len(randomlist)):
  if randomlist[i] == 4:
    d += 1
percent4 = (d/10110)*100

print("4 | " , percent4)

e = 0
for i in range(len(randomlist)):
  if randomlist[i] == 5:
    e += 1
percent5 = (e/10110)*100

print("5 | " , percent5)

f = 0
for i in range(len(randomlist)):
  if randomlist[i] == 6:
    f += 1
percent6 = (f/10110)*100

print("6 | " , percent6)


#make sure the answer is close to 100. Although, because the percentages are rounded it might not be perfect

check = percent1 + percent2 + percent3 + percent4 + percent5 + percent6

print("check- ", check)



