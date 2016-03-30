a = input() # исходный
b = input() # зашифрованный
c = input() # эту зашифровать
d = input() # эту расшифровать
f = dict(zip(a,b))
for i in c:
	if i in f.keys():
		print(f[i], end='')
inv_f = {value: key for key, value in f.items()}
print(f)
print(inv_f)
'''
for j in d:
	if j in f.values():
		print(f.get(key[default]), end='')
'''


'''
abcd
*d%#
abacabadaba
#*%*d*%
'''