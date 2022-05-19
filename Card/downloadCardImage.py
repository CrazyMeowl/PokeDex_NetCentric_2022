import requests
import shutil 
import json
import os

data = json.load(open('sortedCards.json'))
setList = ['Base', 'Other', 'Black & White', 'Sword & Shield', 'HeartGold & SoulSilver', 'XY', 'Sun & Moon', 'Diamond & Pearl', 'E-Card', 'EX', 'Gym', 'Neo', 'NP', 'Platinum', 'POP']

#Make all the folder
for setName in setList:
	largePath = f'{setName}/large'

	os.makedirs(largePath, exist_ok=True)

	smallPath = f'{setName}/small'

	os.makedirs(smallPath, exist_ok=True)


def downloadImage(item):
	file_name = item['id'] + '.png'
	setName = item['set']['series']
	smallURL = item['images']['small']
	largeURL = item['images']['large']

	res = requests.get(largeURL, stream = True)
	if res.status_code == 200:
		with open(f'{setName}/large/{file_name}','wb') as f:
			shutil.copyfileobj(res.raw, f)

	res = requests.get(smallURL, stream = True)
	if res.status_code == 200:
		with open(f'{setName}/small/{file_name}','wb') as f:
			shutil.copyfileobj(res.raw, f)
	return(0)
def cardToIndex(card):
	for i in data:
		if i['id'] == card:
			return data.index(i)
	
total = len(data)
#counter  = int(input('Enter start index: '))
counter = cardToIndex(input('Enter start card\'s id : '))
index = counter - 1
while index < total:
	item = data[index]
	downloadImage(item)
	counter = counter + 1
	os. system('CLS')
	print(f'Lastest Item: {item["id"]}')
	print(f'Downloaded: {counter}, {total - counter} left.')
	print(f'Progess:  {(counter / total)*100}%')
	index += 1

print(data[3914])