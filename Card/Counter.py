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
	try:
		for typeC in item['types']:
			appendWithoutDuplicate(setList,typeC)
	except:
		pass
#print(setList)
#print(len(setList))

#data = json.load(open('card.json'))
#data.sort(key = lambda x: (x['set']['series'],x['set']['id'], x['number']))

data.sort(key = lambda x: (datetime.datetime.strptime(x['set']['releaseDate'], '%Y/%m/%d'),x['set']['id'],x['number']  ))
json_object = json.dumps(data, indent = 4)
with open("sortedCards.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)