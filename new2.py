# словарь, где храним пары namespace:parent_namespace
ns_parentns = {}
# словарь, где храним namespase и список переменных в нем
ns_var = {}
def funk(a, b): # a-неймспейс b-переменная
	for i in ns_var.get(a):
		if i == b:
			return b 
	else:
		funk(ns_parentns.get(a), b)

s = int(input())
for i in range(s):
	cmd, ns, arg = input().split()

# create - создаем пары namespace:parent_namespace	
	if cmd == 'create': 
		ns_parentns[ns] = arg
# add - создаем пары namespace:[список переменных]		
	elif cmd == 'add' and ns not in ns_var.keys():
		ns_var[ns] = []
		ns_var[ns].append(arg)
	elif cmd == 'add' and ns in ns_var.keys():
		ns_var[ns].append(arg)
# отладочный принт, после каждой введеной комманды 
# выводит содержимое словарей
# когда принт коментится - след. if меняется на elif
	print(ns_parentns, ns_var)
	if cmd == 'get':
		funk(ns, arg)
'''
		if ns in ns_var.keys():
#			print(ns_var.get(ns))
			for i in ns_var.get(ns):
				if i == arg:
					print(ns)
					break
				else:
					continue
			if ns in ns_parentns.keys():
'''
'''
		переберем список значений, пока не найдем arg
		если найдем - выводим
		если нет  - находим родителя ns и перебираем у него


#	get foo a

for i in ns_var.get(ns):
	if i == arg:
		print(ns)
		break
	else:
		continue
		'''