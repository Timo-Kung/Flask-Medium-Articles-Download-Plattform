ffimport pymongo


# client = pymongo.MongoClient(['localhost:27017'])
# database = client['test1']

class Database(object):
    url = ['localhost:27017']
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.url)
        Database.DATABASE = client['project']

    @staticmethod
    def insert_one(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def drop(collection):
        Database.DATABASE[collection].drop()
