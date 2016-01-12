import os

t = os.getcwd()

t1 = os.listdir(t)
f = open('All_File.txt','w')
for i in t1:
	t2 = os.path.join(t,i)
	if(os.path.isfile(t2)):
		continue
	if not os.listdir(t2):
		os.rmdir(t2)
	for j in os.listdir(t2):
		t3 = os.path.join(t2,j)
		f1 = open(t3,'r').read()
		f.write(f1)