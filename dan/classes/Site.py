class Site:
    def __init__(self):
        self.db = False  # Объект подключения к БД
        self.request = False   # request aiohttp
        # self.request.method = 'GET' / 'POST' / 'PUT' - метод передачи данных
        self.post = False  # объект post
        self.path = ''  # Путь
        self.p = ''  # Список элементов пути
        self.head = ''  # Материал выводимыей в внутри тега шаблона <head>
        self.tag_title = '' # Тег title
        self.tag_description = '' # Метатег descripton
        self.content = ''  # Основное содержимое
        self.modules = {}  # Словарь модуле
        self.salt = 'DAN_core_salt'  # Соль
        self.settings = ''  # Словарь настроек сайта
