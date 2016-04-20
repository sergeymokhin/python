# 1.4 Пространства имён и области видимости – Шаг 8


# словарь, где храним пары namespace:parent_namespace
ns_parentns = {}
# словарь, где храним namespase и список переменных в нем
ns_var = {}
def funk(ns, arg):
	if ns is None:
		return None
	elif ns_var.get(ns) is None:
		return funk(ns_parentns.get(ns), arg)
	for i in (ns_var.get(ns)):
		if i == arg:
			return ns
	return funk(ns_parentns.get(ns), arg)

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
		print(funk(ns, arg))