import os
import re
import hashlib
import subprocess

#1 
#Напишите скрипт, который читает текстовый файл и выводит символы в порядке убывания частоты встречаемости в тексте. Регистр символа
#не имеет значения. Программа должна учитывать только буквенные символы (символы пунктуации, цифры и служебные символы слудет игнорировать).

def count_letters():
    file = open('task1.txt')
    input_text = file.read()
    file.close()
    dictionary = {i.upper(): input_text.count(i) for i in input_text if i.isalpha()}
    for value in sorted(dictionary.keys(), key=dictionary.get, reverse=True):
        print(value, " --- ", dictionary[value])

count_letters()

#2
#Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках файлы-дубликаты на основе сравнения контрольных сумм (MD5). 
#Файлы могут иметь одинаковое содержимое, но отличаться именами. Скрипт должен вывести группы имен обнаруженных файлов дубликатов. 

def search_duplicate_files():
    file_name = 'task2'
    files = os.listdir(file_name)
    nums = []
    for file in files:
        with open(file_name + '\\' + file) as file:
            nums.append(hashlib.md5(file.read().encode('utf-8')).hexdigest())

    for i in range(len(files) - 1):
        for j in range(i + 1, len(files)):
            if nums[i] == nums[j]:
                print('Группа дубликатов:', files[i], files[j])

search_duplicate_files()

#3
#Задан путь к директории с музыкальными файлами (в названии которых нет номеров, а только названия песен) и текстовый файл,
#хранящий полный список песен с номерами и названиями в виде строк формата «01. Freefall [6:12]». 
#Напишите скрипт, который корректирует имена файлов в директории на основе текста списка песен

def replace_name_track():
    file_name = 'task3'
    with open('task3_track.txt') as f:
        for file in os.listdir(file_name):
            os.replace(file_name + '/' + file, file_name + '/' + f.readline().rstrip() + '.mp3')

replace_name_track()

#4
#Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла, найти в нем с помощью регулярных выражений все
#подстроки определенного вида, в соответствии с вариантом 
#(4 вариант):
#найдите все строки вида «type x = value», где type – это тип (может принимать значение int, short или byte), 
#х – любое слово, value – любое число

def get_data(file_name):
    if os.path.exists(os.getcwd() + '\\' + file_name):
        with open(file_name) as file:
            text = [i for i in file]
        return text


def get_substr(text, reg):
    for i in range(len(text)):
        count = 0
        substr = re.search(reg, text[i])

        while substr != None:
            yield i + 1, substr.string
            count += substr.regs[0][1]
            text[i] = text[i][substr.regs[0][1]:]
            substr = re.search(reg, text[i])


def search_type():
    reg = r'(int|short|byte) \w+ = \d+'
    output_text = 'Строка №{0} : {1}'
    input_text = get_data(input('Введите название файла: '))
    for index, substr in get_substr(input_text, reg):
         print(output_text.format(index, substr))

search_type()


#5
#Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все слова, которые начинаются с большого латинского
#символа (от A до Z) и заканчиваются 2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002». Используйте регулярные выражения

input_text = input('Введите текст: ') #text = 'Petr93 Johnny70 Service2002 5P1234'

def check_input(text, reg):
    for i in range(len(text)):
        parser = re.search(reg,text[i])
        count = 0
        while parser!=None:
            yield i+1,parser.regs[0][0] + count + 1, parser.group()
            count += parser.regs[0][1]
            text[i] = text[i][parser.regs[0][1]:]
            parser = re.search(reg,text[i])

reg = "[A-ZА-ЯЁ][A-ZА-ЯЁa-zа-яё]+([0-9]{4}$|[0-9]{2}$)"
[print(output_text) for i, j, output_text in check_input(input_text.split(),reg)]

#6
#Напишите скрипт reorganize.py, который в директории --source создает две директории: Archive и Small. В первую директорию помещаются
#файлы с датой изменения, отличающейся от текущей даты на количество дней более параметра --days (т.е. относительно старые
#файлы). Во вторую – все файлы размером меньше параметра --size байт. Каждая директория должна создаваться только в случае, если найден
#хотя бы один файл, который должен быть в нее помещен.

#7
#Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома (попурри из коротких фрагментов mp3-файлов в
#пользовательской директории). Для манипуляций со звуковыми файлами можно использовать сторонние утилиты, например, FFmpeg.
#Параметры скрипта:
#--source (-s) – имя рабочей директории с треками, обязателен;
#--destination (-d) – имя выходного файла, необязателен (если не указан, то имя выходного файла – mix.mp3 в директории source);
#--count (-c) – количество файлов в "нарезке", необязателен (если он не указан, то перебираются все mp3-файлы в директории source);
#--frame (-f) – количество секунд на каждый файл, необязателен (если не указан, скрипт вырезает по 10 секунд из произвольного участка каждого файла);
#--log (-l) – необязательный ключ (если этот ключ указывается, то скрипт должен выводить на консоль лог процесса обработки файлов, как в примере);
#--extended (-e) – необязательный ключ (если этот ключ указывается, то каждый фрагмент попурри начинается и завершается небольшим fade in/fade out).


