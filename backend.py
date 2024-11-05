import json

class JsonData:
    def __init__(self, path: str):
        # Opening JSON file
        with open(path) as json_file:
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
import os
DATA = JsonData(os.path.join(os.path.dirname(__file__), 'data.json'))

# Will look for the search term/parameter in the name, brands, and class
# of every entry in JsonData
def search_for(param: str) -> SearchResult:
    param = param.lower()
    results = []
    for name, stats in DATA.iterate():
        if name.lower().__contains__(param):
            results.append(name)
        elif stats['brands'].lower().__contains__(param):
            results.append(name)
        elif stats['clas'].lower().__contains__(param):
            results.append(name)
    
    return SearchResult(True, results=results)

def get_len() -> int:
    return DATA.len()

def get_dict_from_name(name: str) -> dict | None:
    d = DATA.data.get(name.capitalize())
    if d != None:
        return d
    else:
        return None
    
def split_tags(entry: dict) -> list[str]:
    final_tags: list[str] = []
    for tag in entry['tags']:
        # Remove the begining section
        if tag.startswith('<!custom>'):
            final_tags.append(tag[9:])
        elif tag == '<!p>':
            final_tags.append('Do not take this medication while pregnant - it may cause serious complications!')
        elif tag == '<!a>':
            final_tags.append('Do not take this medication with alogol - it may cause serious complications!')
        elif tag == '<!controlled>':
            final_tags.append(
                'This is a controlled substance. Please take caution when dosing and taking this medication. '
                'For help battling addiction, visit: https://americanaddictioncenters.org/'
            )
        else:
            print(f'Unexpected tag: {tag}')

    return final_tags