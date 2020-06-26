import json

data = '{"var1":"harry","var2":"yovi"}'
parsed = json.loads(data)
print(parsed['var1'])