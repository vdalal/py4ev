# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# text processing
print(ord('A'))
print(ord('a'))

# regular expressions
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)
print('------')

import re
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)

print('------')

fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From: ') >= 0:
        print(line)
print('------')

import re
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)

x = 'My 2 favorite numbers are 19, 27, 301 and 42'
y = re.findall('[0-9]+',x)
print(x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)

# greedy matching, max string matching
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)

# non-greedy matching, max string matching
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

x = 'From abcde@xyzwv.com Sat Apr 22 2023 xx:yy:zz'
y = re.findall('\S+@\S+', x)
print(y)

y = re.findall('^From \S+@\S+', x)
print(y)

y = re.findall('^From (\S+@\S+)', x)
print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

x = 'From abcde@xyzwv.com Sat Apr 22 2023 xx:yy:zz'
hostname = re.findall('\S+@(\S+)\s+', x)
print(hostname)

# caret at the beginning of square braces means non-blank
hostname = re.findall('@([^ ]*)', x)
print(hostname)

hostname = re.findall('^From .*@([^ ]*)', x)
print(hostname)

fhandle = open('mbox.txt')
numlist = list()
for line in fhandle:
    line = line.rstrip()
    stuff = re.findall('X-Spam-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue;
    num = float(stuff[0])
    numlist.append(num)

print(numlist)
print('Maximum:', max(numlist))

x = 'We received $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(x)
print(y)