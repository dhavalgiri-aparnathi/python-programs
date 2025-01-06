# Also knows as JSON Encoding

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

json_string = json.dumps(data);

with open("myfi.txt", "w") as file:
    file.write(json_string)
