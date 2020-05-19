def router(SITE):
    print('SYSTEM - router')
    auth = 0

    SITE.content = 'zzzzz'


    if (auth != 1):
        # Если нет авторизации
        if (SITE.method == 'POST' and SITE == 'login'):
            print ('Проверка логина / пароля')
        else:
            print ('Редирект на страницу SYSTEM')

    # CONTENT['component']