from Fraction import*
from Book import*
from Library import*
from Task3 import*
from StringFormatter import*
from Task5 import*
import wx

#Задан простой класс Fraction для представления дробей. Дополнить класс таким образом, чтобы выполнялся код.

def task1():
    frac = Fraction (7, 2)
    print('Дробь = ', frac)
    print('Унарный минус = ', -frac)
    print('Инверсия = ', ~frac)
    print('Возведение в степень = ', frac**2)
    print('Приведение к float = ', float(frac))
    print('Приведение к int = ', int(frac))

task1()

#Напишите классы «Книга» (с обязательными полями: название, автор, код), «Библиотека» (с обязательными полями: адрес, номер) и
#корректно свяжите их. Код книги должен назначаться автоматически при добавлении книги в библиотеку (используйте для этого
#статический член класса). Если в конструкторе книги указывается в параметре пустое название, необходимо сгенерировать исключение
#(например, ValueError). Книга должна реализовывать интерфейс Taggable с методом tag(), который создает на основе строки набор тегов
#(разбивает строку на слова и возвращает только те, которые начинаются с большой буквы). Например, tag() для книги с названием
#‘War and Peace’ вернет список тегов [‘War’, ‘Peace’]. Реализуйте классы таким образом, чтобы корректно выполнялся код.

def task2():

    lib = Library(1, '51 Some str., NY')
    lib += Book.Book('Leo Tolstoi', 'War and Peace')
    lib += Book.Book('Charles Dickens', 'David Copperfield')

    for book in lib:
        print(book._id)
        print(book)
        print(book.tag())

task2()

#Создайте графическую оболочку для скрипта, написанного в ходе выполнения задания № 4 лабораторной работы № 2, в виде диалогового
#окна. Рекомендуется использовать wxPython или PyQt

def task3():

    app = wx.App()
    frame = Task3()
    frame.Show()
    app.MainLoop()

task3()

#Напишите простой класс StringFormatter для форматирования строк со следующим функционалом:
#– удаление всех слов из строки, длина которых меньше n букв;
#– замена всех цифр в строке на знак «*»;
#– вставка по одному пробелу между всеми символами в строке;
#– сортировка слов по размеру;
#– сортировка слов в лексикографическом порядке

def task4():

    text = 'Tim1 Pike 19Svetlana23 Leo David56 Charles Jk Cho Lera'

    format = StringFormatter();
    print(text)
    print(format.del_word(text, 5))
    print(format.replace_digit(text))
    print(format.insert_space(text))
    print(format.sort_size(text))
    print(format.sort_alphabet(text))

task4()

#Напишите скрипт с графическим интерфейсом пользователя для демонстрации работы класса StringFormatter. Разные комбинации
#отмеченных чекбоксов приводят к разным цепочкам операций форматирования задаваемой в верхнем поле строки с разными результатами

def task5():

    app = wx.App()
    frame = Task5()
    frame.Show()
    app.MainLoop()

task5()
