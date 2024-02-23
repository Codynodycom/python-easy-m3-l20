import methods


def regulator(method, input_text):
    """
        Функция выбирает нужный метод, 
        обрабатывает сообщение
        и возвращает результат
    """

    output_text = ''
    # Шифрование
    output_text = methods.ENCRYPT[method](input_text)
    
    return output_text
    
        
def is_wrong_input(method):
    try:
      if 1 <= int(method) <= 7:
          return False
      return True
    except Exception as e:
        print('ERROR:', e)
        return True