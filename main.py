# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# text processing
print(ord('A'))
print(ord('a'))

# Tuples
fhandle = open('mbox.txt')
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:5]:
    print(key, val)

# very short alternative to the algo above
c = {'a': 10, 'c': 2, 'b': 14}
print(c)
print(sorted( [ (v,k) for k,v in c.items() ] ) )


d = {'c': 10, 'a': 1, 'b': 30}
print(d.items())
print(sorted(d.items()))

for k, v in sorted(d.items()):
    print(k, v)

tmp = list()
for k, v in sorted(d.items()):
        tmp.append((v, k))

print(tmp)
tmp = sorted(tmp, reverse=False)
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 10, 13)
print(y)
print(max(y))

lst = list()
print(dir(lst))

tup = tuple()
print(dir(tup))

(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

d = dict()
d['aaa'] = 2
d['bbb'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000) < (0, 3, 2))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))


fhandle = open('mbox.txt')
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('bigword =', bigword, 'bigcount =', bigcount)


counts = { 'aaa' : 1 , 'bbb' : 3, 'ccc': 100, 'ddd': 10}
for key in counts:
    print(key, counts[key])

# Get a list of keys
print('List of keys:', list(counts))
print('List of keys using keys function', counts.keys())

# Get list of values
print('List of values:', counts.values())

print('List of items:', counts.items())

for aaa, bbb in counts.items():
    print(aaa, bbb)


fileWordList = dict()
# lineWords = list()
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    lineWords = line.split()
    for word in lineWords:
     fileWordList[word] = fileWordList.get(word, 0) + 1

print(fileWordList)

maxCount = 0
maxKey = 'None'
for word in fileWordList:
    if fileWordList[word] > maxCount:
        maxCount = fileWordList[word]
        maxKey = word
    print(word, '\t\t|\t', fileWordList[word])

print('Word which occurs most often =', maxKey, '|', maxCount)

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

counts = dict()
names = ['aaa', 'bbb', 'ccc', 'ddd', 'aaa']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

counts = dict()
names = ['alice', 'bob', 'charlie', 'damon', 'alice']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


dictX = {"Fri": 20, "Thu": 6, "Sat": 1}
print(dictX)

dictX["Thu"] = 13
dictX["Sat"] = 2
dictX["Sun"] = 9
print(dictX)

# dictionary literals
jjj = {'chuck' : 1, 'fred' : 2, 'jan' : 3}
print(jjj)

ooo = { }
print(ooo)

# dictionary
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 20
print(purse)
print('Purse with key candy', purse['candy'])
purse['candy'] = purse['candy'] + 2
print('Purse with key candy', purse['candy'])
print(purse)

# Lists
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue;
    words = line.split()
    print(words[2])

email = words[1]
print(email)

domain = email.split('@')
print('Domain =', domain[1])


line = 'a lot                of spaces'
stuffList = line.split()
print(len(stuffList))

line = 'first;second;third'
stuffList = line.split()
print(len(stuffList))
print(stuffList)

line = 'first;second;third'
stuffList = line.split(';')
print(len(stuffList))
print(stuffList)


abc = 'with three words'
stuffList = abc.split()
print(stuffList)
print(len(stuffList))
print(stuffList[1])

for w in stuffList:
    print(w)


total = 0
count = 0
while True:
    inp = input('Please enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average: ', average)

numlist = list()
while True:
    inp = input('Please enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print('List length:', len(nums))
print('List max:', max(nums))
print('List min:', min(nums))
print('List sum:', sum(nums))
print('List avg:', sum(nums)/len(nums))


friends = ['Joe', 'Bob', 'Alice']
print('List:', friends)
friends.sort()
print('List sorted:', friends)

stuff = list()
stuff.append('book')
stuff.append(99)
print('List stuff:', stuff)
stuff.append('cookie')
print('List stuff:', stuff)

x = list()
print(dir(x))

xlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dir(xlist))

z = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('List z elements 1 and upto 3', z[1:3])
print('List z elements upto 4', z[:4])
print('List z elements from 5 till the end', z[5:])
print('List z elements from beginning till the end', z[:])

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print('List a: ', a)
c = a + b
print('List c: ', c)

friends = ['Alice', 'Bob', 'Charlie', 'Dean']

for friend in friends:
    print('Happy New Year', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)

print(range(4))
list = ['Alice', 'Bob', 'Charlie', 'Dean']
print('Length of list:', len(list))
print('Range of list:', range(len(list)))

list = [2, 4, 6, 8, 12, 14, 16]
print('Original list:', list)
list[2] = 17
print('Modified list:', list)
print('List length:', len(list))


list = ['Alice', 'Bob', 'Charlie', 'Dean']
print(list)
for val in list:
    print(val)

list2 = [101, 'Alice', 9.7, 'Zee', [2, 4, 8], 19]
for val in list2:
    print(val)

fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('From: '):
        count = count + 1
print('There were', count, 'subject lines in ', fname)


fhandle = open('mbox.txt', 'r')
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhandle = open('mbox.txt', 'r')
inp = fhandle.read()
print(len(inp))
print(inp)
print('First 20 chars =:', inp[:20])
fhandle.close()

fhandle = open('mbox.txt', 'r')
print(fhandle)
count = 0
for line in fhandle:
    count = count+1
    print(count, line)
print('Line count =', count)



data = 'From stephen.zz@uct.ac.zn Sat Jan 6 xx.yy.zz 2023'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

greet = '    Hello Bob      '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

oldstr = 'Hello Bob'
newstr = oldstr.replace('Bob', 'Jane')
print(oldstr)
print(newstr)
newstr = oldstr.replace('o', 'Y')
print(newstr)


fruit = 'banana'
pos = fruit.find('na')
print('Position of na =', pos)
pos = fruit.find('z')
print('Position of z =', pos)


greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))


fruit = 'banana'
if 'n' in fruit:
    print('true')
else:
    print('false')

fruit = 'banana'
if 'nan' in fruit:
    print('true')
else:
    print('false')

a = 'Hello'
b = 'There'
print(a+b)

c = a + ' ' + b
print(c)

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

print(s[:2]) # eliminate the beginning of the string
print(s[8:]) # eliminate the end of the string
print(s[:])


fruit = 'banana'
for letter in fruit:
    print(letter)
print('Length of fruit =', len(fruit))

fruit = 'banana'
print('Length of fruit =', len(fruit))

smallest = None
for value in [19, 9, 16, 23, 3, 32, 17, 12]:
    if smallest is None:
        smallest = value
    if value < smallest:
        smallest = value

    print('smallest =', smallest)


zork = 0
print('zork =', zork)
for thing in [9, 16, 23, 32, 17, 12]:
    zork = zork + 1
    print(zork, thing)
print('zork =', zork)

numbers = [3, 41, 12, 9, 17, 74, 15]

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print('Max =', max)

friends = ['alice', 'bob', 'charlie']

for friend in friends:
    print('Happy Birthday', friend)

for i in [5, 4, 3, 2, 1, 0]:
    print(i)
print('Blastoff!')

n = 5
while n > 0:
    print(n)
    n = n-1
print('blastoff!')
print(n)

while True:
    line = input('> ')
    if line == 'done':
       break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

def addtwo (x, y):
    sum = x + y
    return sum

x = addtwo(3,5)
print(x)

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('es')
greet('en')
greet('fr')

def some_function():
    print('hello')
    print('fun')

print('hello world')
some_function()
print('zip')
some_function()
print('done')

big = max('Hello world World') # lowercase > uppercase characters
print(big)
small = min('hello world World')
print(small)

print (float(99)/100)

i = 42
type(i)
f = float(i)
print(f)

strVal = '123'
type(strVal)
# print(strVal + 1)

iVal = int(strVal)
print(iVal)
print(iVal + 1)


for i in range(10):
    if i % 2 == 0:
        print(i, ' :even')
    else:
        print(i, ' :odd')

x = 3

if x < 2:
    print('small')
elif x < 3:
    print('medium')
else:
    print('large')

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

eu_floor = input('EU floor: ')
us_floor = int(eu_floor) + 1
print('US floor: ', us_floor)

name = input('Enter your name: ')
print('Hello', name)


