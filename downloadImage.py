import requests # request img from web
import shutil # save img locally4
import json
data = json.load(open('resource/all-gen.json'))
'''
url = 'https://play.pokemonshowdown.com/sprites/bw/bulbasaur.png'
file_name = 'resource/texture/Zeraora.png'

res = requests.get(url, stream = True)

if res.status_code == 200:
	with open(file_name,'wb') as f:
		shutil.copyfileobj(res.raw, f)
	print('Image sucessfully Downloaded: ',file_name)
else:
	print('Image Couldn\'t be retrieved')
'''
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
