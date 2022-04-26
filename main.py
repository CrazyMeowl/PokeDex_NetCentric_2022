import json
data = json.load(open('resource/all-gen.json'))
#print(data)
#Name, ID, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Sprite
genIdList = [(1,151),(152,251),(252,386),(387,493),(494,649),(650,721),(722,807)]
#for i in data:
#	print(i['Pokemon'])
def searchByName(inString):
	idList = []
	for i in data:
		if inString in i['pokemon']:
			idList.append(i['ID'])
	return idList

def getByID(inId):
	chosenOne = data[inId-1]
	info = ""
	for i in chosenOne:
		info = info + "%10s :  %s  \n"%(i,str(chosenOne[i]))
	#print(info)
	return info
def getGen(gen):
	#print(genIdList[gen-1])
	startId,endId = genIdList[gen-1]
	for i in range(startId,endId+1):
		print(getByID(i))
hehe = searchByName(input("Enter to search: "))
for i in hehe:
	print(getByID(i))