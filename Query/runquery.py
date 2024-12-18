import pymongo
from query import getquery

mongodb_uri = "<MONGODB_URI>"
mongo_client = pymongo.MongoClient(mongodb_uri)


def execute():
    query = getquery()
    values = {'$set': {'roteiroConstaEmFaturaEntregador': True}}
    mongo_client['entregas']['roteiro'].update_many(query, values)


execute()
