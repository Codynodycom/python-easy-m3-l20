from utils import regulator, is_wrong_input
from constants import (
    START_MESSAGE,
    ENCRYPT_METHOD
    )


working = True
current_mode = None
method = None
input_text = None
output_text = None
is_restart = False


while input(START_MESSAGE) != 'ознакомился':
    print()

while working:
    method = input(ENCRYPT_METHOD)
    # проверка ввода
    if is_wrong_input(method=method):
        continue
   
    # получение исходного текста от пользователя
    input_text = input('Введите текст:\n>>>')

    # обработка данных и получение результата
    output_text = regulator(
        method=method, 
        input_text=input_text
    )
    print('Зашифрованный текст:')
    print(output_text + '\n')
    current_mode = None
    method = None
    
    # Перезапустить или выйти
    if input('Перейти в главное меню? (0 - выйти)\n>>>') == '0':
       break
    
print('\033[31mДешифратор звершил работу.\n\n')


