import jinja2
import aiohttp_jinja2
from aiohttp import web
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
    print(SITE.path, SITE.method)

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
    print(SITE.path, SITE.method)

    system.router(SITE)
    print('SITE.content -> ', SITE.content)

    auth = 1
    return {'AUTH': auth, 'content': SITE.content}


async def edit(request):
    # Режим визуального редактирования
    path = request.match_info.get('url', "Anonymous")
    REQ = {'path': path, 'method': 'get'}
    print(request)
    text = 'EDIT - Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return web.Response(text=text)

def site(request):
    SITE = Site()
    path = request.match_info.get('url', '')
    SITE.path = path
    SITE.p = path.split('/')
    SITE.method = 'GET'

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