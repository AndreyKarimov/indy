import json
from string import ascii_lowercase

json_string = dict([(ascii_lowercase[i], i + 1) for i in range(len(ascii_lowercase))])
json_data = json.dumps(json_string)
print(json_data)
