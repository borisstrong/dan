def router(request):
    print('SYSTEM - router')
    path = request.match_info.get('url', '')

    print(request.method)
    print(path)
    auth = 0

    if (auth != 1):
        # Если нет авторизации
        if (request.method == 'POST' and path == 'login'):
            print ('Проверка логина / пароля')
        else:
            print ('Редирект на страницу SYSTEM')
