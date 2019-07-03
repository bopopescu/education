#добавление значения по умолчанию для аргументов
# при создании универсальной функции на примере использования множеств
def search4letters(phrase: str, letters: str='aeiou') -> set: #аргументу letters присвоено значение по умолчанию
        """Возвращает множество букв из 'letters', найденных 
        в указанной фразе"""
        return set(letters).intersection(set(phrase))
#функцию можно еще вызывать так
#search4letters(letters='duckins', phrase='iu')
#при чем порядок расположения аргументов не важен
