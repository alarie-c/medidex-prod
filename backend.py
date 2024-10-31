import json

class JsonData:
    def __init__(self, path: str):
        # Opening JSON file
        with open('data.json') as json_file:
            self.data: dict = json.load(json_file)

        if self.data == {}:
            print('Fatal Error :: data.json experienced an error while loading.')
            print('\tdata.json is empty!')
            exit(1)

    def iterate(self):
        return self.data.items()
    
    def len(self):
        return self.data.__len__()
    
    def dump(self):
        for x in self.data:
            print(x)
    
class SearchResult:
    def __init__(self, success: bool, **kwargs):
        self.success = success
        self.results = kwargs['results']

    # Returns int(0) when search result success is False
    # Returns the results when able
    def unwrap(self) -> list | int:
        if self.success:
            return self.results
        else:
            return 0
        
    def len(self):
        return self.results.__len__()
        
############################################################################################
# Functions (accessible from the frontend)
############################################################################################
        
# CONSTANT DATA FILE -- RESULT OF JSON PARSING
DATA = JsonData('data.json')

# Will look for the search term/parameter in the name, brands, and class
# of every entry in JsonData
def search_for(param: str) -> SearchResult:
    results = []
    for name, stats in DATA.iterate():
        if name.__contains__(param):
            results.append(name)
        elif stats['brands'].__contains__(param):
            results.append(name)
        elif stats['clas'].__contains__(param):
            results.append(name)
    
    return SearchResult(True, results=results)

def get_len() -> int:
    return DATA.len()

def get_dict_from_name(name) -> dict | None:
    d = DATA.data.get(name)
    if d != None:
        return d
    else:
        return None