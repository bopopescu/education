from flask import Flask, render_template, request, escape #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from vsearch6 import search4letters

from DBmc import UseDatabase

app = Flask (__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',   #Flask использует словарь app.config. Добавляем его.
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:        #req передает объект запроса
    """Функция журналирует веб-запрос в БД и возвращает результаты"""
    """Теперь используем диспетчер контекста UseDatabase, которому передаем
        настройки app.config"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)""" # создзаем строку с текстом запроса для записи в БД
        cursor.execute(_SQL, (req.form['phrase'],   #выполняем запрос
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,   #из строки с описанием браузера извлекается только его название
                              res,))
    
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
        """Извлекает данные из запроса, выполняет поиск, возвращает результаты"""
        phrase = request.form['phrase']
        letters = request.form['letters']
        title = 'Here are your results:'
        results = str(search4letters(phrase, letters))
        log_request(request,results)    #вызов функции журналирования
        return render_template('results.html', 
                               the_phrase = phrase,
                               the_letters = letters,
                               the_title = title,
                               the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
        """Выводит  HTML форму"""
        return render_template('entry.html', the_title='Welcome to search4letters web!')

@app.route('/viewlog')  #будем читать лог со страницы
def view_the_log() -> 'html':      #объявляем новую функцию
        """Выводит содержимое файла журнала в виде HTML таблицы"""
        with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """select phrase, letters, ip, browser_string, results 
                                from log"""
                """отправляем запрос на сервер
                затем извлекаем результаты (присваиваются
                переменной contents"""        
                cursor.execute(_SQL)
                contents = cursor.fetchall()
        
        """определяем имена столбцов"""
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        
        return render_template ('viewlog.html',
                                the_title='View log',
                                the_row_titles=titles,
                                the_data=contents,)

if __name__ == '__main__':      #позволяет запускать вебприл. локально
        app.run(debug=True) #режим отладки автомато перезапускает вебсервер если видит изменения
