import wmiotdata

# wmiotdata.put_latestdata(22, 33)

import json

json_data = '{"humid": 47, "temp": 17}'
python_obj = json.loads(json_data)
print
python_obj["name"]
print
python_obj["city"]