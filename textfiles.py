class TextFileReader:
    '''A simple text file reader'''
    text = None
    path = None 
    teste = '123'

    def __init__(self, path):
        '''Creating an object with the path of the file'''
        self.path = path 
        textFile = open(self.path, 'r')
        self.text = textFile.read() 
        textFile.close() 

    def __str__(self):
        return self.path    
