import sys
sys.path.append('system/catalog/classes')
from classes.Catalog import Catalog


def insert(SITE):
    print('FUNCTION -> system-> calalog -> cat -> insert')
    #print(SITE.request.method)
    print('INS => ')
    print(SITE.post)
    print(SITE.post['url'])

    CATALOG = Catalog(SITE)

    if CATALOG.checkUrl(SITE.post['url']) is not None:
        SITE.content += '<h1>Ошибка</h1><div>url <b>' + SITE.post['url'] + '</b> - занят!</div>'
        return

    
    # CATALOG.insert(data)
    # print(SITE.db.execute("INSERT INTO component SET component = 'catalog', `name` = 'shop', `type` = 'catalog', settings = '', ordering = 7"))
    """
    sql = "INSERT INTO component SET component = 'catalog', `name` = %s, `type` = 'catalog', settings = '', ordering = 7"
    SITE.db.execute(sql, ('shop'))
    """