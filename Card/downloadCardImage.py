import requests
import shutil 
import json
import os

data = json.load(open('sortedCards.json'))

setList = [['base1', 102], ['base2', 64], ['base3', 62], ['base4', 130], ['base5', 83],
 ['base6', 110], ['basep', 53], ['bp', 9], ['bw1', 115], ['bw10', 105], ['bw11', 140], 
 ['bw2', 98], ['bw3', 102], ['bw4', 103], ['bw5', 111], ['bw6', 128], ['bw7', 153], 
 ['bw8', 138], ['bw9', 122], ['bwp', 101], ['cel25', 25], ['cel25c', 25], ['col1', 106], 
 ['dc1', 34], ['det1', 18], ['dp1', 130], ['dp2', 124], ['dp3', 132], ['dp4', 106], 
 ['dp5', 100], ['dp6', 146], ['dp7', 106], ['dpp', 56], ['dv1', 21], ['ecard1', 165], 
 ['ecard2', 182], ['ecard3', 182], ['ex1', 109], ['ex10', 145], ['ex11', 114], ['ex12', 93], 
 ['ex13', 111], ['ex14', 100], ['ex15', 101], ['ex16', 108], ['ex2', 100], ['ex3', 100], 
 ['ex4', 97], ['ex5', 102], ['ex6', 116], ['ex7', 111], ['ex8', 108], ['ex9', 107], 
 ['fut20', 5], ['g1', 117], ['gym1', 132], ['gym2', 132], ['hgss1', 124], ['hgss2', 96], 
 ['hgss3', 91], ['hgss4', 103], ['hsp', 25], ['mcd11', 12], ['mcd12', 12], ['mcd14', 12], 
 ['mcd15', 12], ['mcd16', 12], ['mcd17', 12], ['mcd18', 12], ['mcd19', 12], ['mcd21', 25], 
 ['neo1', 111], ['neo2', 75], ['neo3', 66], ['neo4', 113], ['np', 40], ['pl1', 133], 
 ['pl2', 120], ['pl3', 153], ['pl4', 111], ['pop1', 17], ['pop2', 17], ['pop3', 17], 
 ['pop4', 17], ['pop5', 17], ['pop6', 17], ['pop7', 17], ['pop8', 17], ['pop9', 17], 
 ['ru1', 16], ['si1', 18], ['sm1', 173], ['sm10', 238], ['sm11', 261], ['sm115', 69], 
 ['sm12', 272], ['sm2', 180], ['sm3', 177], ['sm35', 81], ['sm4', 126], ['sm5', 178], 
 ['sm6', 150], ['sm7', 187], ['sm75', 80], ['sm8', 240], ['sm9', 198], ['sma', 94], 
 ['smp', 251], ['swsh1', 216], ['swsh2', 209], ['swsh3', 201], ['swsh35', 80], ['swsh4', 203], 
 ['swsh45', 73], ['swsh45sv', 122], ['swsh5', 183], ['swsh6', 233], ['swsh7', 237], 
 ['swsh8', 284], ['swsh9', 186], ['swsh9tg', 30], ['swshp', 210], ['tk1a', 10], ['tk1b', 10], 
 ['tk2a', 12], ['tk2b', 12], ['xy0', 39], ['xy1', 146], ['xy10', 129], ['xy11', 116], 
 ['xy12', 113], ['xy2', 110], ['xy3', 114], ['xy4', 124], ['xy5', 164], ['xy6', 112], 
 ['xy7', 101], ['xy8', 165], ['xy9', 126], ['xyp', 216]]



'''
		
	#print(f'{path}{file_name}')

baseURL = 'https://images.pokemontcg.io/'
for item in setList:
	print(f'{setList.index(item)}: {item[0]}')

setID = int(input('Please enter set INDEX ( number ): '))
res = int(input('0: Low Res | 1: Hi Res | 2: Both : '))

setName = setList[setID][0]
total = setList[setID][1]
counter = 0
i = 1

largePath = f'{setName}/large'

os.makedirs(largePath, exist_ok=True)

smallPath = f'{setName}/small'

os.makedirs(smallPath, exist_ok=True)



os. system('CLS')
while i <= total:

	url = baseURL+f'{setName}/{i}'
	if res == 0 or res == 1:
		print(url)
		if res == 0:
			url = url + '.png'
			path = smallPath
		if res == 1:
			url = url + '_hires.pngs'
			path = largePath
		print(url)
		

		file_name = f'/{setName}-{str(i)}.png'
		print(file_name)

		download(url,path,file_name)
		counter = counter + 1
		print(f'Downloaded: {counter}.')
		print(f'{total - counter} left')
		
	elif res == 2:
		url1 = url + '.png'
		url2 = url + '_hires.png'
		file_name = f'/{setName}-{str(i)}.png'
		print(file_name)
		download(url1,path,file_name)
		file_name = f'/{setName}-{str(i)}.png'
		print(file_name)
		download(url2,path,file_name)
		counter = counter + 1
		os. system('CLS')
		print(f'Downloaded: {counter}.')
		print(f'{total - counter} left')
	i = i + 1


'''
#Make all the folder
for item in setList:
	setName = item[0]
	largePath = f'{setName}/large'

	os.makedirs(largePath, exist_ok=True)

	smallPath = f'{setName}/small'

	os.makedirs(smallPath, exist_ok=True)


def downloadImage(item):
	file_name = item['id'] + '.png'
	setName = item['set']['id']
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

total = len(data)
counter  = int(input('Enter start index: '))
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