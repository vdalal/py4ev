# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# urllib, web socket library (chapter 11)
import urllib.request, urllib.parse, urllib.parse

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    print(line.decode().strip())

counts = dict()
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# read a web page
fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhandle:
    print(line.decode().strip())


# text processing
print(ord('A'))
print(ord('a'))

# sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# mysock.connect('www.dr-chuck.com/page1.htm')
print(mysock)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0 \n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()