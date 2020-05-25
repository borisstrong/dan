class Catalog:
    def __init__(self, SITE):
        self.db = SITE.db

    def getItems(self):
        self.db.execute("SELECT * FROM component ORDER BY ordering")
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False
    
    def checkUrl(self, url):
        sql = "SELECT id FROM component WHERE url = %s LIMIT 1"
        self.db.execute(sql, url)

        return self.db.fetchone()


    """
    def insertData(self, data):
        pass

    def getItem(self, id):
        pass
    """

    """
    def deleteCatalog(self):
        pass

    def deleteCatalog(self):
        pass

    def updateData(self, data):
        pass

    def updateSettings(self, data):
        pass
    """