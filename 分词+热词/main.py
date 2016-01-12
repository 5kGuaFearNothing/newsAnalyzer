#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
from Chose import *
from Cnt import *
F = open('Temp.txt','w')
def CUT(f):
	s = jieba.cut_for_search(f)
	return ' '.join(s)
t = os.getcwd()
t1 = os.path.join(t,'20130111')
t2 = os.listdir(t1)
for i in t2:
	t3 = os.path.join(t1,i)
	f = open(t3,'r')
	f = f.readline()
	F.write(CUT(f))
F = open('Temp.txt','r')
F1 = Chose(F)
F1 = open('Temp1.txt','r')
Cnt(F1)