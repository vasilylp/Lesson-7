"""Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:                                                 Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам                Парам пам-пам """

# def count_vowel(frases_VP):
#     vowels = []
#     for i in frases_VP:
#         vowel = 0
#         for j in i:
#             if j in 'аеиоуэюя':
#                 vowel += 1
#         vowels.append(vowel)
#     return vowels
#
#
#
# def check_vowel(vowels):
#     check = vowels[0]
#     c = 0
#     for z in range(1, len(vowels)):
#         if vowels[z] == check:
#             c += 1
#         else:
#             c = 0
#             break
#     return c
#
#
#
#
# frases_VP = input("Введите фразы через пробел : ").split()
# count_vowels = count_vowel(frases_VP)
# if check_vowel(count_vowels) == 0:
#     print("Пам парам")
# else:
#     print("Парам пам-пам")

# 2 solution_______________________________
def count_vowel(frases_VP):
    vowels = []
    for i in frases_VP:
        vowel = 0
        for j in i:
            if j in 'аеиоуэюя':
                vowel += 1
        vowels.append(vowel)
    return vowels



def check_vowel(vowels):
    if vowels.count(vowels[0]) == len(vowels):
        print("Парам пам-пам")
    else:
        print("Пам парам")



frases_VP = input("Введите фразы через пробел : ").split()
count_vowels = count_vowel(frases_VP)
check = check_vowel(count_vowels)
