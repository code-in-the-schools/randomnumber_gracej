#make a list for 10,100,10000
import random
randomlist = []
for i in range(1,10):
  n = random.randint(1,6)
  randomlist.append(n)

randomlist2 = []
for i in range(1,100):
  n = random.randint(1,6)
  randomlist2.append(n)

randomlist3 = []
for i in range(1,10000):
  n = random.randint(1,6)
  randomlist3.append(n)


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

print("# or iterations: 100")

a = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 1:
    a += 1
percent1 = (a)

print("1 | " , percent1)

b = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 2:
    b += 1
percent2 = (b)

print("2 | " , percent2)

c = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 3:
    c += 1
percent3 = (c)

print("3 | " , percent3)

d = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 4:
    d += 1
percent4 = (d)

print("4 | " , percent4)

e = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 5:
    e += 1
percent5 = (e)

print("5 | " , percent5)

f = 0
for i in range(len(randomlist2)):
  if randomlist2[i] == 6:
    f += 1
percent6 = (f)

print("6 | " , percent6)


#repeat for 10000
print("number of iterations: 10000")

a = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 1:
    a += 1
percent1 = (a/100)

print("1 | " , percent1)

b = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 2:
    b += 1
percent2 = (b/100)

print("2 | " , percent2)

c = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 3:
    c += 1
percent3 = (c/100)

print("3 | " , percent3)

d = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 4:
    d += 1
percent4 = (d/100)

print("4 | " , percent4)

e = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 5:
    e += 1
percent5 = (e/100)

print("5 | " , percent5)

f = 0
for i in range(len(randomlist3)):
  if randomlist3[i] == 6:
    f += 1
percent6 = (f/100)

print("6 | " , percent6)



###

#ask for user input of any numbers 0-9

num= input("enter some numbers with the characters 0-9: ")

#figure out the rate of each number
z = 1
for i in range(len(num)):
  if num[i] == 1:
    z += 1
percent1 = (z/100)

print("1 | " , percent1)


#convert into a list

#have the computer choose a number and repeat for 10 

#repeat for 100

#repeat for 100000








