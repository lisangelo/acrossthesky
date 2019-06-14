from abc import ABC, abstractmethod

class BD(ABC):
    '''Implements an BD interface'''

    _user = None
    _password = None 
    _data_base = None
    _server_address = None 

    def __str__(self):
        description = "Address: " + self._server_address 
        description += " User: " + self._user 
        description += " Password: " + self._password 
        description += " Database: " + self._data_base
        return description 

    def getServerAddress(self):
        '''Informs the server address'''
        return self._server_address

    def getUser(self):
        '''Informs the user'''
        return self._user

    def getPassword(self):
        '''Informs the password'''
        return self._password

    def getDatabase(self):
        '''Informs the database name'''
        return self._data_base

    def connect(self, server_address, user, password, data_base):
        '''Get the information to connect'''
        self._user = user 
        self._password = password 
        self._data_base = data_base
        self._server_address = server_address 

    @abstractmethod
    def close(self):
        '''Close the connection with the database'''
        raise NotImplementedError

    @abstractmethod
    def query(self, command):
        '''Send a query to database and provides an result'''
        raise NotImplementedError

    @abstractmethod
    def change(self, command):
        '''Send a command to change the data'''
        raise NotImplementedError

    @abstractmethod
    def save(self):
        '''Save the modifications'''
        raise NotImplementedError

    @abstractmethod
    def discard(self):
        '''Discard the modifications'''
        raise NotImplementedError

