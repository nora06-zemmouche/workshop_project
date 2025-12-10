import mongomock


class MongoDBClient:
    def __init__(self, db_name="test_db"):
        self.client = mongomock.MongoClient()
        self.db = self.client[db_name]

    def insert(self, collection_name, document):
        return self.db[collection_name].insert_one(document)

    def find(self, collection_name, query):
        return list(self.db[collection_name].find(query))
