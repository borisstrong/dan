class Site:
    def __init__(self):
        self.method = 'GET'  # Метод передачи данных
        self.req = ''  # Полная строка запроса
        self.path = ''  # Путь
        self.p = ''  # Список элементов пути
        self.head = ''  # Материал выводимыей в внутри тега шаблона <head>
        self.tag_title = '' # Тег title
        self.tag_description = '' # Метатег descripton
        self.content = ''  # Основное содержимое
        self.modules = {}  # Словарь модуле
        self.salt = 'DAN_core_salt'  # Соль
        self.settings = ''  # Словарь настроек сайта
