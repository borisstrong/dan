def insert(SITE):
    print('FUNCTION -> system_> calalog -> cat -> insert')
    #print(SITE.request.method)
    print('INS => ')
    print(SITE.post)
    print(SITE.post['sef'])
    # print(SITE.db.execute("INSERT INTO component SET component = 'catalog', `name` = 'shop', `type` = 'catalog', settings = '', ordering = 7"))
    sql = "INSERT INTO component SET component = 'catalog', `name` = %s, `type` = 'catalog', settings = '', ordering = 7"
    SITE.db.execute(sql, ('shop'))