from mysqlutils import MySQLDB 

print("Conectando ao banco de dados")
mysql = MySQLDB("localhost", "acrossthesky_admin", "julio_verne", "acrossthesky")

mysql.connect() 

result = mysql.query("select count(*) from lixo where id = '1'")
if result[0][0] == 0: #nao encontrado
    mysql.change("insert into lixo values ('1')")
else:
    mysql.change("update lixo set id = 2 where id = '1'")

mysql.save()

mysql.close()
