#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
L = {}
D = set()
Screen_Table = open('Screen_Table.txt','r')
Screen_Table = Screen_Table.read()
# Screen_Table=Screen_Table.encode('utf-8')
Screen_Table = Screen_Table.split()
for i in Screen_Table:
	if i not in D:
		D.add(i)
		print i

def Cnt(f,F):
	f = f.read()
	f = map(str,f.split())
	for i in f:
		if i in D:
			continue
		if  i not in L:
			L[i] = 1;
		else:
			L[i] += 1
	T = sorted(L.iteritems(), key=lambda d:d[1], reverse = True )
	for i in T:
		s = str(i[0])+':'+str(i[1])
		F.write(s)
		F.write('\n')