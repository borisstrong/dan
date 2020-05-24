from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
from edit import edit
from insert import insert
from cat_list import cat_list


def cat(SITE):
    print('PATH -> system/catalog/cat')

    # Вызов функций по ключу
    functions = {
        '': cat_list,
        'edit': edit,
        'add': edit,
        'insert': insert
        # 'update': update,
        # 'delete': delete,
        # 'settings_edit': settings_edit,
        # 'settings_update': settings_update
    }

    print('SITE.p[2] = ', SITE.p[2])

    if (SITE.p[2] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    functions[SITE.p[2]](SITE)
