from random import choice
from constants import (
    RU_TO_MORZE_DICT, EN_TO_MORZE_DICT,
    RU_TO_SYMBOLS_DICT, RU_ALPHABET_CEASAR,
    RU_ALPHABET, EN_ALPHABET, MORZE_TO_EN_DICT,
    MORZE_TO_RU_DICT, KEY, GRID_KEY
)

def text_to_caesar_cipher(input_text):
    print('Шифрование методом Цезаря...')
    shift = 3
    # Создаем обратный словарь для отображения порядковых номеров в русские буквы
    reverse_alphabet = {v: k for k, v in RU_ALPHABET_CEASAR.items()}

    # Переводим текст в нижний регистр
    text = input_text.lower()
    # Подготавливаем пустую строку для зашифрованного текста
    encrypted_text = ''

    # Проходим по каждой букве в тексте
    for char in text:
        # Если символ не является буквой, добавляем его в зашифрованный текст без изменений
        if char not in RU_ALPHABET_CEASAR:
            encrypted_text += char

        else:
            # Получаем порядковый номер текущей буквы
            char_index = RU_ALPHABET_CEASAR[char]
            # Применяем сдвиг к порядковому номеру с учетом длины алфавита
            shifted_index = (char_index + shift) % len(RU_ALPHABET_CEASAR)
            # Получаем зашифрованную букву из обратного словаря
            encrypted_char = reverse_alphabet[shifted_index]
            # Добавляем зашифрованную букву к зашифрованному тексту
            encrypted_text += encrypted_char

    return encrypted_text


def text_to_simple_substitution_cipher(input_text):
    encrypted_text = ''

    for char in input_text:
        if char.lower() in RU_ALPHABET:
            index = RU_ALPHABET.index(char.lower())
            encrypted_char = KEY[index] if char.islower() else KEY[index].upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text


def text_to_vigenere_cipher(input_text):
    # Проверяем, что текст и ключ не пустые
    if not input_text or not KEY:
        return "Текст и ключ не могут быть пустыми"
    
    # Приводим текст и ключ к нижнему регистру
    text = input_text.lower()
    key = KEY.lower()
    # Подготавливаем пустую строку для зашифрованного текста
    encrypted_text = ''
    # Переменная для отслеживания позиции символа в ключе
    key_index = 0
    
    # Проходим по каждому символу в тексте
    for char in text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Находим смещение для текущей буквы в тексте
            shift = ord(key[key_index]) - ord('а')
            # Зашифровываем текущий символ с помощью смещения
            encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            # Добавляем зашифрованный символ к зашифрованному тексту
            encrypted_text += encrypted_char
            # Переходим к следующему символу в ключе
            key_index = (key_index + 1) % len(key)

        else:
            # Если символ не является буквой, оставляем его без изменений
            encrypted_text += char
    
    return encrypted_text


def text_to_block_cipher(input_text):
    # Проверяем, что текст не пустой
    if not input_text:
        return "Текст не может быть пустым"
    
    # Приводим текст к нижнему регистру и удаляем все пробелы
    text = input_text.lower().replace(" ", "")
    # Подготавливаем пустую строку для зашифрованного текста
    encrypted_text = ''
    
    # Проходим по каждому символу в тексте
    for char in text:
        # Получаем числовое значение ASCII для текущего символа
        ascii_value = ord(char)
        # Добавляем к зашифрованному тексту две цифры: первая - количество цифр в ASCII-коде, вторая - сам ASCII-код
        encrypted_text += str(len(str(ascii_value))) + str(ascii_value)
    
    return encrypted_text


def text_to_morze(input_text):
    morse_phrase = ''
    
    for letter in input_text.lower():
        if letter in RU_TO_MORZE_DICT:
            morse_phrase += RU_TO_MORZE_DICT[letter] + ' '
        else:
            morse_phrase += ' '

    return morse_phrase.strip()


ENCRYPT = {
    '1': text_to_caesar_cipher,
    '2': text_to_simple_substitution_cipher,
    '3': text_to_vigenere_cipher,
    '4': text_to_block_cipher,
    '5': text_to_morze,
}
