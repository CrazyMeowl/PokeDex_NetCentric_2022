import requests
import shutil 
import json
data = json.load(open('sortedCards.json'))
counter = 0
for item in data:
	counter += 1
	url = item['images']['large']

	file_name = f'{item["set"]["id"]}/'+str(item['id'])+'.png'
	print(file_name)
	
	res = requests.get(url, stream = True)

	if res.status_code == 200:
		with open(file_name,'wb') as f:
			shutil.copyfileobj(res.raw, f)
			print(item['name'])
	print(f'Counter: {counter}')