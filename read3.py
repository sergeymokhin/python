mat = 0
phys = 0
rus = 0
strok = 0
with open('dataset_3363_4.txt', 'r') as s:
	for line in s.readlines():
		s1 = line.strip().split(';')
		#print(s1[1], s1[2], s1[3])
		print((int(s1[1]) + int(s1[2]) + int(s1[3])) / (len(s1)-1))
		mat += int(s1[1])
		phys += int(s1[2])
		rus += int(s1[3])
		strok += 1
print(mat/strok, phys/strok, rus/strok)