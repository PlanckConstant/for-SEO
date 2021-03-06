'''
from pprint import pprint
from requests_html import HTMLSession

session = HTMLSession()
resp = session.get(f'http://dveriross.ru/mezhkomnatnye-dveri')

title = str(resp.html.xpach('//title/text()'))
description = resp.html.xpach('//meta[@name="description"]')
description = str(description).split('<Element \'meta\' content=')
description = str(description).split('name=\'description\'>')
h1 = resp.html.xpach('//h1/text()')

print('title: ' + title)
print('description: ' + description)
print('h1: ' + h1)
'''


######### list: ##########


var = ['wdwdwdwdwdwd', '1312414214214214214', [1,2,3,5,5, ['w','w',3,5,'6f','eff','et34t4rg','dgf422rf','3r'], 'wfw', 'ww'],'wd']

print(var[2][4]) #Внутри 2го списка 4й элемент
#5
print(var[0][4])
#'w'
print(var[3])
#'wd'
print(var[1])
#'1312414214214214214'
print(var[2])
#[1, 2, 3, 5, 5, ['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r'], 'wfw', 'ww']
print(var[2][5])
#['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r']
print(var[2][5][2])
#3


var.append('qwerty') # добавляет элемент в конец списка. прелбразует существующий список
var.clear # очистка списка
a = var.copy() # создаст физически другую копию списка. У каждой копии свой ID
bar = var # создаст копию списка. У каждой копии единый ID
tar = bar # при изменении одного списка остальные тоже меняются
var.count() # считает количество вхождений (не считает во вложенных списках)
var.split() # разбивает строки на списки слов
var.split
s = 'список доменов, список урл, список ключевых слов, список html страниц'
print(s.split())
# ['список', 'доменов,', 'список', 'урл,', 'список', 'ключевых', 'слов,', 'список', 'html', 'страниц']
print(s.split().count('урл,'))
# 1
s.replace(',', '').upper() # замена
'СПИСОК ДОМЕНОВ СПИСОК УРЛ СПИСОК КЛЮЧЕВЫХ СЛОВ СПИСОК HTML СТРАНИЦ'
var.index('1312414214214214214')
#1
var[2]
# '1312414214214214214'
len(var) # длина любого итерируемого списка
#4
var.insert(1, 555) # добавляет элемент со сдвигом остальных
# ['wdwdwdwdwdwd', 555, '1312414214214214214', [1, 2, 3, 5, 5, ['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r'], 'wfw', 'ww'], 'wd']
var.append(444) # добавляет элемент в конец списка
# ['wdwdwdwdwdwd', 555, '1312414214214214214', [1, 2, 3, 5, 5, ['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r'], 'wfw', 'ww'], 'wd', 444]
555 in var # проверяет наличие чего-то внутри чего-то
# true
var.pop # возвращает последний элемент списка, удаляя его из списка
# 444
# ['wdwdwdwdwdwd', 555, '1312414214214214214', [1, 2, 3, 5, 5, ['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r'], 'wfw', 'ww'], 'wd']
remove # удалаяет элэмент из списка
var.reverse() # переворачивает список, не меняя ID
var = var[::-1] # переворачивает список меняя ID
list('123456') # разбивает строку на список
# ['1', '2', '3', '4', '5', '6']
'123234235232'.split('2') # разбивает строку на список по символу
# ['1', '3', '34', '35', '3', '']
r = [2, 4 ,5 ,65, 34, 345, 2, 6, 6, 7 ,9]
r.sort() #сортирует список
# [2, 2, 4, 5, 6, 6, 7, 9, 34, 65, 345]


###### КОРТЕЖ (tuple)  #######
# неизмняемый тип данных
kort  = var = (123111115, 1312414214214214214, 87, 786,2576)
# поддеррживаются все методы списков, кроме изменяющих.

kort = list(kort) # для сортировки и изменения данных перегоняем кортеж в список
kort.sort() # сортируем
# [87, 786, 2576, 123111115, 1312414214214214214]
kort = tuple(kort) # и обратно в кортеж
# (87, 786, 2576, 123111115, 1312414214214214214)

#список в кортеже можно изменять как угодно.
kort1 = (87, 786, 2576, 123111115,['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r'], 1312414214214214214)
kort1[4].append('qwerty') # добваляем элемент в конец списка в кортеже
# (87, 786, 2576, 123111115, ['w', 'w', 3, 5, '6f', 'eff', 'et34t4rg', 'dgf422rf', '3r', 'qwerty'], 1312414214214214214)

######## Распаковка кортежа #######
kort2 = (0,1,2,3,4)
a, b, c, d, e = kort2
# a = 0
# b = 1
# c = 2
# d = 3
# e = 4

t = a, b, c, d, e # запаковка кортежа

###### обмен значений 2х переменных #######

a = 100
b = 200

a, b = b, a # создаётся кортеж и переприсваевается


rt = 1,2,3,4,5,5685,89,345,14 # бюбой набор переменных, написанных через запятую интерпритатор воспринимает как кортеж
# (1,2,3,4,5,5685,89,345,14)

####### Множества (set) ########
# тоже массив, но в него записываются только уникальные значения
# слайсы ииндексы не работают
st = {1,2,3,4,5,45}
# .append не работает здесь
 # {1,2,3,4,5,10,45}

st.add((1,2,6)) # можно добавить внутрь кортеж, но не список
# {1, 2, 3, 4, 5, 45, (1, 2, 6)}

hash(123) # конвертирует в ХЕШ. Множества работают по хешам и очень быстро

br = {1,2,3}

st - br # вычитание множеств. Складывать нельзя (+)
# {45, 4, 5, (1, 2, 6)}

st.union(br)
# {1, 2, 3, 4, 5, 45, (1, 2, 6)}

# Методы множеств возвращают копии объекта, не меняя сам объект. Объекты остаются неизменными.

st.difference(br) # То же, что и (-)

st.difference_update(br) # То же, что и (-), но сохраняет изменения в объекте

st.discart(br) # ???

st.intersection(br) # пересечения множеств
# {1, 2, 3}

