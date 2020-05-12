import jinja2
import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def index(request):
    # Основной режим вывода содержимого
    path = request.match_info.get('url', "Anonymous")
    REQ = {
        'path': path,
        'p': path.split('/'),
        'method': 'get'
    }
    print(request)
    print(REQ['p'])
    text = 'Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return {'test_1': 'TEST 1', 'test_2': 'TEST 2'}
    # return web.Response(text=text)

async def ws(request):
    # Веб-сокеты
    pass


async def system(request):
    # Админка
    path = request.match_info.get('url', "Anonymous")
    REQ = {'path': path, 'method': 'get'}
    print(request)
    text = 'SYSTEM - Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return web.Response(text=text)


async def edit(request):
    # Режим визуального редактирования
    path = request.match_info.get('url', "Anonymous")
    REQ = {'path': path, 'method': 'get'}
    print(request)
    text = 'EDIT - Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return web.Response(text=text)


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes([web.static('/templates', 'templates'),
                web.static('/media', 'media'),
                web.get('/ws', ws),  # Веб-сокеты
                web.get('/edit/{url:.*}', edit),  # Режим визуального редактирования
                web.get('/system/{url:.*}', system),  # Админка
                web.get('/{url:.*}', index)])

if __name__ == '__main__':
    web.run_app(app)