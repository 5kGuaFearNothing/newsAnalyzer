#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
from Chose import *
from Cnt import *

def gao(data):
	F = 'T_Divid_' + data +'.txt'
	F1 = 'T_Rm_Again_' + data + '.txt'
	F2 = data + '_Result' + '.txt'

	def CUT(f):
		s = jieba.cut_for_search(f)
		return ' '.join(s)
	t = os.getcwd()
	t1 = os.path.join(t,data)
	t2 = os.listdir(t1)
	FF = open(F,'w')
	for i in t2:
		t3 = os.path.join(t1,i)
		f = open(t3,'r')
		f = f.readline()
		FF.write(CUT(f))

	f = open(F,'r')
	FF1 = open(F1,'w')
	f = Chose(f,FF1)
	f = open(F1,'r')
	FF2 = open(F2,'w')
	Cnt(f,FF2)
	FF.close()
	FF1.close()
	f.close()
	os.remove(F)
	os.remove(F1)

Path = os.getcwd()
Path_list = os.listdir(Path)
for i in Path_list:
	ii = os.path.join(Path,i)
	if os.path.isfile(ii):
		continue;
	gao(i)
