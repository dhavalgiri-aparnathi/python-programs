# Also known as JSON Decoding

import json

json_string = '''
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    } 
'''

data = json.loads(json_string)

print(data)
