from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def getSQLCommand(self):
        raise NotImplementedError

    def replaceLastOccurance(self, text, last_char, new_char):
        pos = text.rfind(last_char)
        new_text = text[:pos] + new_char + text[pos + len(last_char):]
        return new_text  

class Insert(Command):
    '''Creates an insert sql command from text and dictionaries'''

    _table_name = None
    _dict_record = None
    _sql_command = None 

    def __init__(self, table_name, dict_record):
        self._table_name = table_name 
        self._dict_record = dict_record 

    def getSQLCommand(self):
        '''Returns a fully formated sql command, ready for use'''
        if self._dict_record != None:
            self.__commandFromDict()

        return self._sql_command        

    def __commandFromDict(self):
        self._sql_command = 'insert into ' + self._table_name +  ' ('
        for i in self._dict_record:
            self._sql_command += i + ', '
        self._sql_command = Command.replaceLastOccurance(self, self._sql_command, ',', ')') 
        self._sql_command += 'values ('    
        for i in self._dict_record:
            _field = self._dict_record[i]
            if _field == None:
                self._sql_command += 'null, '
            else:    
                self._sql_command += "'" + _field + "', "
        self._sql_command = Command.replaceLastOccurance(self, self._sql_command, ',', ')') 
        self._sql_command += ';'  

class Update(Command):
    '''Creates an update sql command from text and dictionaries'''

    _table_name = None
    _dict_record = None
    _dict_key = None
    _sql_command = None 

    def __init__(self, table_name, dict_record, dict_key):
        self._table_name = table_name 
        self._dict_record = dict_record
        self._dict_key = dict_key  

    def getSQLCommand(self):
        '''Returns a fully formated sql command, ready for use'''
        if self._dict_record != None:
            self.__commandFromDict()

        return self._sql_command        

    def __commandFromDict(self):
        self._sql_command = 'update ' + self._table_name +  ' set '
        for i in self._dict_record:
            self._sql_command += i + ' = ' 
            _field = self._dict_record[i]
            if _field == None:
                self._sql_command += ' null, '
            else:    
                self._sql_command += "'" + _field + "', "
        self._sql_command = Command.replaceLastOccurance(self, self._sql_command, ',', '')
        self._sql_command += 'where '
        for i in self._dict_key:
            self._sql_command += i + ' = ' 
            _field = self._dict_key[i]
            if _field == None:
                self._sql_command += ' null and '
            else:    
                self._sql_command += "'" + _field + "' and "
        self._sql_command = Command.replaceLastOccurance(self, self._sql_command, 'and', '')
        self._sql_command += ';'  

class Count(Command):
    '''Returns the amount of records corresponding to keys'''

    _table_name = None
    _dict_key = None
    _sql_command = None 

    def __init__(self, table_name, dict_key):
        self._table_name = table_name
        self._dict_key = dict_key 

    def getSQLCommand(self):
        '''Returns a fully formated sql command, ready for use'''
        if self._table_name != None:
            self.__commandFromDict()

        return self._sql_command        

    def __commandFromDict(self):
        self._sql_command = 'select count(*) from ' + self._table_name
        if self._dict_key != None: 
            self._sql_command += ' where '
            for i in self._dict_key:
                self._sql_command += i + ' = ' 
                _field = self._dict_key[i]
                if _field == None:
                    self._sql_command += ' null and '
                else:    
                    self._sql_command += "'" + _field + "' and "
            self._sql_command = Command.replaceLastOccurance(self, self._sql_command, 'and', '')
        self._sql_command += ';'  
