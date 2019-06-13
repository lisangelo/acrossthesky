from textfiles import TextFileReader
from jsonutils import JSONParser 
from sqlutils import Insert, Update, Count 

TABLE_NAME = 'satcat'
KEY_FIELDS = ["INTLDES", "NORAD_CAT_ID", "OBJECT_TYPE"]

fr = TextFileReader('satcat.txt')
print('Lendo arquivo', fr)
print('------------------------------')

json_parser = JSONParser(fr.getContent())

dict_satcat = json_parser.json_to_dict()
for r in dict_satcat:
    print(r[KEY_FIELDS[0]])
    insert = Insert(TABLE_NAME, r)
    print(insert.getSQLCommand())
    dict_keys = {}
    for d in KEY_FIELDS:
        dict_keys.update({d : r[d]})
    update = Update(TABLE_NAME, r, dict_keys)
    print(update.getSQLCommand()) 
    count = Count(TABLE_NAME, dict_keys)
    print(count.getSQLCommand()) 