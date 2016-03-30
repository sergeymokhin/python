#https://stepic.org/lesson/Файловый-вводвывод-3363/step/2
import re

with open('dataset_3363_2.txt', 'r') as s:
	s1 = s.readline().strip()
base = re.split('(\d*)', s1)
i = 0
for element in range (0, len(base)-1, 2):
    if base[i] == base[-2]:
        break
    base[i] = base[i]*int(base[i+1])
    print(base[i], end='')
    i = i + 2