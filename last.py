d = {}
with open('dataset_3380_5.txt', 'r') as s1:
	for line in s1.readlines():
		s = line.strip().split()
		s[0] = int(s[0])
		s[2] = int(s[2])
		if s[0] not in d.keys():
			d[s[0]] = [0, 1]
			d[s[0]][0] += s[2]
		elif s[0] in d.keys():
			d[s[0]][0] += s[2]
			d[s[0]][1] += 1
d2 = {key: value[0]/value[1] for key, value in d.items()}
#print(d2)
l = d2.keys()
l = list(l)
l.sort()
for i in l:
	print (i, ' ', d2[i],end='\n')