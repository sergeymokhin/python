n = int(input())
coords = [0, 0]
for i in range(0, n):
	s = input().split()
	s[1] = int(s[1])
	if s[0] == 'sever':
		coords[1] += s[1]
	elif s[0] == 'zapad':
		coords[0] -= s[1]
	elif s[0] == 'jug':
		coords[1] -= s[1]
	elif s[0] == 'vostok':
		coords[0] += s[1]
print (coords[0], coords[1])