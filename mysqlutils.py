from bdutils import BD 
import pymysql 

class MySQLDB(BD):

    _db = None 
    _cursor = None 

    def connect(self, server_address, user, password, data_base):
        BD.connect(self, server_address, user, password, data_base)
        self._db = pymysql.connect(BD.getServerAddress(self), 
                                   BD.getUser(self), 
                                   BD.getPassword(self), 
                                   BD.getDatabase(self))
        self._cursor = self._db.cursor()

    def close(self):
        self._db.close()

    def query(self, command):
        data = None
        self._cursor.execute(command)
        data = self._cursor.fetchall()

        return data       

    def change(self, command):
        self._cursor.execute(command)

    def save(self):
        self._db.commit()

    def discard(self):
        self._db.rollback()

