import json
import os




genIdList = [(1,151),(152,251),(252,386),(387,493),(494,649),(650,721),(722,807)]
#for i in data:
#	print(i['Pokemon'])
# Return a list of pokemon that match the search string


class Pokemon():
	#load pokemon data from json file
	data = json.load(open('resource/all-gen.json'))
	#Pokemon attribute: Name, ID, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed, Sprite
	def __init__(self,inData):
		self.Name = inData['Name']
		self.ID = inData['ID']
		self.Type1 = inData['Type1']
		self.Type2 = inData['Type2']
		self.Ability1 = inData['Ability1']
		self.Ability2 = inData['Ability2']
		self.Ability3 = inData['Ability3']
		self.HP = inData['HP']
		self.Attack = inData['Attack']
		self.Defense = inData['Defense']
		self.SpecialAttack = inData['SpecialAttack']
		self.SpecialDefense = inData['SpecialDefense']
		self.Speed = inData['Speed']
		self.Sprite = inData['Sprite']
	#Get the pokemon List
	def getAll():
		return Pokemon.data



	def searchPokeByName(inString):
		idList = []
		for i in Pokemon.data:
			if inString.lower() in i['pokemon'].lower():
				idList.append(i['ID'])
		return idList
	#get pokemon name by id return info string
	def getPokeByID(inId):
		chosenOne = Pokemon.data[inId-1]
		return chosenOne

	def getGen(gen):

		startId,endId = genIdList[gen-1]
		for i in range(startId,endId+1):
			print(getPokeByID(i))



'''
while True:
	for i in searchByName(input("Enter to search: ")):
		print(getByID(i))
'''

row = 0
col = 0

'''
while row < 18:
	col = 0
	while col < 18:	
		print(f'[{typeList[row]}][{typeList[col]}]: {typeChart[row][col]}')
		col = col + 1
	row = row + 1 

print(getPokeByID(10))
test = Pokemon(getPokeByID(10))
'''
