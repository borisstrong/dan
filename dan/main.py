import jinja2
import aiohttp_jinja2
from aiohttp import web
import pymysql
import pymysql.cursors
import sys
sys.path.append('classes')
from classes.Site import Site
sys.path.append('system')
import system


@aiohttp_jinja2.template('index/index.html')
async def index(request):
    # Основной режим вывода содержимого
    SITE = site(request)
    print('************************************')

    return {'test_1': 'TEST 1', 'test_2': 'TEST 2'}
    # return web.Response(text=text)

async def ws(request):
    # Веб-сокеты
    pass


@aiohttp_jinja2.template('system/main.html')
async def system_r(request):
    # Админка
    SITE = site(request)
    print('************************************')

    SITE.post = await request.post()  # Ждём получение файлов методом POST
    system.router(SITE)

    auth = 0

    return {'AUTH': auth, 'content': SITE.content}


async def edit(request):
    # Режим визуального редактирования
    path = request.match_info.get('url', "Anonymous")
    print(request)
    text = 'EDIT - Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return web.Response(text=text)


def site(request):
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='dan_py',
        charset='utf8mb4',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )
    SITE = Site()
    SITE.db = con.cursor()
    path = request.match_info.get('url', '')
    SITE.path = path
    SITE.p = path.split('/')
    i = len(SITE.p)
    while i < 7:
        SITE.p.append('')
        i += 1
    SITE.request = request

    return SITE



app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes([web.static('/templates', 'templates'),
                web.static('/media', 'media'),
                web.get('/ws', ws),  # Веб-сокеты
                web.get('/edit/{url:.*}', edit),  # Режим визуального редактирования
                web.get('/system/{url:.*}', system_r),  # Админка
                web.post('/system/{url:.*}', system_r),  # Админка
                web.get('/{url:.*}', index)])

if __name__ == '__main__':
    web.run_app(app)