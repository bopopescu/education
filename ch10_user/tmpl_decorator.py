"""Универсальный шаблон для использования как основа для новых декораторов"""
from functools import wraps #обяз.имп-ть ф-ю, кот.является декоратором из стандартной библиотеки

def decorator_name(func):
    @wraps(func)    #декорируем ф-ю wrapper с пом.декоратора wraps
    def wrapper(*args, **kwargs):  #вложенная строка def означает начало вложенной функции wrapper
                                    #*args, **rwargs позволяет принимать ф-ии wrapper любое кол-во аргументов
        # 1. Code to execute BEFORE calling the decorator function
        # 2. Вызов декорируемой функции и возврат
        #    полученных от нее результатов
            return func(*args, **kwargs)    #...вызвать декорируемую функцию  
            
        # 3. Код для выполнения ВМЕСТО вызова декорируемой функции
        
    return wrapper  #возвращаем вложенную функцию