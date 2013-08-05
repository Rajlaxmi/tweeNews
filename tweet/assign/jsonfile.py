import json
config = json.loads(open('indiamonth.txt').read())
print config["statuses"][0]
