import requests
import shutil 
import json
import datetime
data = json.load(open('sortedCards.json'))

illegalList = ['#','%','&','{','}','\\','/','$','<','>','*','?','!','+','`','\'','\"',':','|','=','@']
def appendWithoutDuplicate(inList,inItem):
	if inItem not in inList:
		inList.append(inItem)
setList = []
for item in data:
	appendWithoutDuplicate(setList,(item['set']['series'],item['set']['id'],item['set']['releaseDate']))
for item in setList:
	print(item)
#print(setList)
#print(len(setList))

#data = json.load(open('card.json'))
#data.sort(key = lambda x: (x['set']['series'],x['set']['id'], x['number']))

data.sort(key = lambda x: (datetime.datetime.strptime(x['set']['releaseDate'], '%Y/%m/%d'),len(x['set']['id']),x['set']['id'],len(x['number']),x['number']))

json_object = json.dumps(data, indent = 4)

with open("sortedCards2.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

