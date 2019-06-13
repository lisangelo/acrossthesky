import json

class JSONParser:
    '''Very straight-forward parser to json'''     
    original_text = None
    def __init__(self, text):
        '''Sets the orginal text'''
        self.original_text = text 

    def json_to_dict(self):
        '''Returns a dictionary with the json content'''
        return json.loads(self.original_text)    