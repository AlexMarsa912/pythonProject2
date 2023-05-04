# Задание 1
side = 4  # Сторона квадрата
perimeter = 4 * side  # Периметр квадрата
square = 4 * side  # Площадь квадрата
diagonal = 2 ** 0.5 * side  # Диагональ квадрата
print(perimeter, square, diagonal)

# Задание 2
a = 5
b = 7
c = 2
D = b ** 2 - 4 * a * c  # Диsdvbgasdbgfrsefrhнант должен быть больше нуля
x1 = (-b + D ** 0.5) / 2 * a
x2 = (-b - D ** 0.5) / 2 * a
print(x1, x2)

#  Задание 3
string1 = 'Мал ерш, да колюч'
string2 = 'Не пойманная рыба всегда большой кажется'
string3 = string1 + ' ' + string2
print(string3)
print(string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:])

# Задание 4
path = 'D:\Фото\Image.jpg'  # Абсолютный путь к файлу
disk = list(path.split("\\"))[0]  # Разделение строки на список и выделение переменной с названием диска
root_folder = list(path.split("\\"))[1]  # Разделение строки на список и выделение переменной с названием корневой папки
file = list(path.split("\\"))[2]  # Разделение строки на список и выделение переменной с названием файла с расширением
print('Название файла без расширения ' + file[:file.find('.')] + ',' + 'название диска ' + disk[0] + ',' + ' название корневой папки ' + root_folder)

#  Задание 5
a = 7
b = 8
c = a + b
result1 = "%d + %d = %d" % (a, b, c)  # Форматирование с использованием оператора %
print(result1)
c = a * b
result2 = "{} * {} = {}".format(a, b, c)  # Форматирование с использованием метода format()
print(result2)

# Задание 6
string1 = 'Рыбак рыбака видит издалека'
print(string1[0:len(string1):2])

# Задание 7
string1 = 'ruv'
string2 = 'kjhrsdfvnaouqzm'
simbol1 = string2.find(string1[0])
simbol2 = string2.find(string1[1])
simbol3 = string2.find(string1[2])
print(string2[min(simbol1, simbol2, simbol3):(max(simbol1, simbol2, simbol3) + 1)])
