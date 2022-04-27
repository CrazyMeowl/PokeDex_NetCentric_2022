import requests 
import shutil 
import json
data = json.load(open('resource/all-gen.json'))

for item in data:
	#print(item['Sprite'],'resource/texture/'+item['pokemon']+'.png')
	url = item['Sprite']
	file_name = 'resource/texture/'+str(item['ID'])+'.png'
	print(file_name)
	
	res = requests.get(url, stream = True)

	if res.status_code == 200:
		with open(file_name,'wb') as f:
			shutil.copyfileobj(res.raw, f)
			print(item['pokemon'])
