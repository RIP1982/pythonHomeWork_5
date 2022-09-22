# Создайте программу для игры в ""Крестики-нолики"".

matrix = []

for i in range(1, 10):
   matrix.append(i)
print(matrix)

def board(matrix): # Функция для отрисовки поля 3х3
   print('-'*13)
   for i in range(3):
      print('|', matrix[0+i*3], '|', matrix[1+i*3], '|', matrix[2+i*3], '|')
      print('-'*13)


def input_(token): # Функция  принимающая от игрока № ячейки(ход)
   value = False
   while not value:
      player_move = input('Укажите ячейку для ввода ' + token + ' ! ') # Принимаем номер ячейки
      try:
         player_move = int(player_move) # Проверяем, что ввели число
      except:
         print('Ошибка ввода') # Отрабатываем ошибку ввода(не число)
         continue
      if player_move >= 1 and player_move <= 9: # Проверка на диапозон ввода(1-9)
         if (str(matrix[player_move-1]) not in 'XO'): # Проверка, занята ли ячейка
            matrix[player_move - 1] = token
            value = True
         else:
            print('Это поле занято!')
      else:
         print('Такого поля не существует!')

def check(matrix): # Функция проверки
   # Создаем кортеж выигрышных ячеек
   win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
   for each in win_combination:
      if matrix[each[0]] == matrix[each[1]] == matrix[each[2]]: # Если все 3 символа равны возвращаем символ(line 54)
         return matrix[each[0]]
   return False

def main_part(matrix): # Функция основная
   winner = False
   counter = 0
   while not winner:
      board(matrix)
      if counter%2 == 0: # Четный ход Х, нечетный О
         input_('X')
      else:
         input_('O')
      counter+=1
      if counter > 4: # После 5 хода запускается проверка на выигрыш
         temp = check(matrix)
         if temp:
            print(temp, 'Победа!')
            winner = True
            break
      if counter == 9: # после 9 хода и проверки на выигрыш, объявляется ничья
            print('Ничья')
            winner = False
            break
   board(matrix)

main_part(matrix)












