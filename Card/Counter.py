import requests
import shutil 
import json

data = json.load(open('sortedCards.json'))

illegalList = ['#','%','&','{','}','\\','/','$','<','>','*','?','!','+','`','\'','\"',':','|','=','@']

for item in data:
	for ill in illegalList:
		if ill in item['id']:
			print(item['id'])