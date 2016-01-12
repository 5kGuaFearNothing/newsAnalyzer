#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
F = open('Aim.txt','w')
L = {}
def Cnt(f):
	f = f.read()
	f = map(str,f.split())
	for i in f:
		if  i not in L:
			L[i] = 1;
		else:
			L[i] += 1
	T = sorted(L.iteritems(), key=lambda d:d[1], reverse = True )
	for i in T:
		s = str(i[0])+':'+str(i[1])
		F.write(s)
		F.write('\n')