# #https://stepic.org/lesson/Файловый-вводвывод-3363/step/3
with open('dataset_3363_3.txt', 'r') as st:
	s = st.read().strip()
#s = 'abc a bCd bC AbC BC BCD bcd ABC'
sl = s.lower()
a = sl.split(' ')
a.sort() # сортировка нужна, чтобы вывести лексикографически первое 
#print(a) # принт для проверки, не нужен
x = 0 # счетчик вхождений
y = '' # переменная для сохранения элемента
for i in range (0, len(a)):
    if a.count(a[i]) > x:
        x = a.count(a[i])
        y = a[i]
print(y, x, end =' ')