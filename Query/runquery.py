import pymongo
from query import getquery

mongodb_uri = "mongodb+srv://diegomoreira:SRmTpIYdzaCvFBIQOC@asaplog-development-pri.2rgxp.mongodb.net/?retryWrites=true&w=majority"
mongo_client = pymongo.MongoClient(mongodb_uri)


def execute():
    query = getquery()
    values = {'$set': {'roteiroConstaEmFaturaEntregador': True}}
    mongo_client['entregas']['roteiro'].update_many(query, values)


execute()
