'''
	if cmd == 'get':
		rev_d = dict((v, k) for k, vals in ns_var.items() for v in vals)
		print(rev_d)
'''



'''
# поступают комманды трех типов:

create <namespace> <parent> –  +
создать новое пространство имен с именем <namespace> 
внутри пространства <parent>

add <namespace> <var> –  +
добавить в пространство <namespace> переменную <var>

get <namespace> <var> – 
получить имя пространства, 
из которого будет взята переменная <var> 
при запросе из пространства <namespace>, 
или None, если такого пространства не существует
'global':'None'
'''