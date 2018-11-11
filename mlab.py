import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds021969.mlab.com:21969/cookids

host = "ds021969.mlab.com"
port = 21969
db_name = "cookids"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())