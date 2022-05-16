import requests
import shutil 
import json
def get_id(item):
	return item["id"]

def appendWithoutDuplicate(inList,inItem):
	if [inItem,0] not in inList:
		inList.append([inItem,0])

data = json.load(open('card.json'))
data.sort(key=get_id)
json_object = json.dumps(data, indent = 4)
with open("sortedCards.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)
'''
for i in data[0]
	print()

setList = []
for item in data:
	appendWithoutDuplicate(setList,item['set']['id'])
for item in setList:
	counter = 0
	for ITEM in data:
		if ITEM['set']['id'] == item[0]:
			counter += 1
	item[1] = counter
	print(item)
'''