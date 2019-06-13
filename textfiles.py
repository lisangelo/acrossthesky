class TextFileReader:
    '''A simple text file reader'''
    _text = None
    _path = None 

    def __init__(self, path):
        '''Creating an object with the path of the file'''
        self._path = path 
        textFile = open(self._path, 'r')
        self._text = textFile.read() 
        textFile.close() 

    def __str__(self):
        return self._path    

    def getContent(self):
        '''Returns content of text file'''
        return self._text     
