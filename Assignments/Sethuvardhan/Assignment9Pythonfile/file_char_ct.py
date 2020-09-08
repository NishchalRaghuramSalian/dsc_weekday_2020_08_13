import sys

k = sys.argv

d = {}

if len(k) >= 2:
	with open(k[1],'r') as fl:
		data = fl.read()
	sp_ct = 0
	print(repr(data))
	for k in data:
		d[k] = d.get(k,0) + 1
	for k,v in d.items():
		print('{} : {}'.format(repr(k), v))
else:
	print('File name not entered')