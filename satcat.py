from textfiles import TextFileReader
from jsonutils import JSONParser 
from sqlutils import Insert, Update, Count 
from mysqlutils import MySQLDB

TABLE_NAME = 'satcat'
KEY_FIELDS = ["INTLDES", "NORAD_CAT_ID", "OBJECT_TYPE"]

fr = TextFileReader('satcat.txt')
print('Lendo arquivo', fr)
print('------------------------------')

json_parser = JSONParser(fr.getContent())

dict_satcat = json_parser.json_to_dict()

#connecting to the db
db = MySQLDB() 
db.connect("localhost", "acrossthesky_admin", "julio_verne", "acrossthesky")

for r in dict_satcat:
    #criar as chaves
    keys = {}
    for d in KEY_FIELDS:
        keys.update({d : r[d]})
    
    #informat id principal
    print(r[KEY_FIELDS[0]])

    #pesquisar se existe
    count = Count(TABLE_NAME, keys).getSQLCommand()
    result = db.query(count)
    if result[0][0] == 0: #inserir
        insert = Insert(TABLE_NAME, r).getSQLCommand()
        print(insert)
        db.change(insert)
    else: #alterar    
        update = Update(TABLE_NAME, r, keys).getSQLCommand()
        print(update)
        db.change(update)

db.save() 
db.close()
