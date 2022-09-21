# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Я очнулся от забвения в Зимбабве под звуки горна!'
letters = 'абв'
new_string = list(filter(lambda x: letters not in x, string.split()))
print(string)
print(' '.join(new_string))