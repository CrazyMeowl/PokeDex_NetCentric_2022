import json
import os
data = json.load(open('resource/all-gen.json'))

pokemonData = json.load(open('resource/all-gen.json'))
abilityData = json.load(open('resource/abilities.json'))
typeList = ['NORMAL','FIGHTING','FLYING','POISON','GROUND','ROCK','BUG','GHOST','STEEL','FIRE','WATER','GRASS','ELECTRIC','PSYCHIC','ICE','DRAGON','DARK','FAIRY'] 


genIdList = [(1,151),(152,251),(252,386),(387,493),(494,649),(650,721),(722,807)]
#for i in pokemonData:
#	print(i['Pokemon'])
# Return a list of pokemon that match the search string

#Pokemon attribute: Name, ID, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed, Sprite
class Pokemon():
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

#Move attribute: Name, Type, Category, Power, Accuracy, PowerPoint, Effect, Chance
class Ability():
	def __init__(self,inData):
		self.Name = inData['Name']
		self.Type = inData['Type']
		self.Category = inData['Category']
		self.Power = inData['Power']
		self.Accuracy = inData['Accuracy']
		self.PowerPoint = inData['PowerPoint']
		self.Effect = inData['Effect']
		self.Chance = inData['Chance']


def searchPokeByName(inString):
	idList = []
	for i in pokemonData:
		if inString.lower() in i['pokemon'].lower():
			idList.append(i['ID'])
	return idList
#get pokemon name by id return info string
def getPokeByID(inId):
	chosenOne = pokemonData[inId-1]
	return chosenOne

def getGen(gen):

	startId,endId = genIdList[gen-1]
	for i in range(startId,endId+1):
		print(getPokeByID(i))

def getAllAbilities():
	for i in abilityData:
		for a in i:
			print(a,":",i[a],end="|")
		print()
def getAbility(inString):
	for ability in abilityData:
		if inString.lower() in ability['Name'].lower():
			return ability
def searchAbilitiesByName(inString):
	abilityList = []
	for i in abilityData:
		if inString.lower() in i['Name'].lower():
			abilityList.append(i['Name'])
	return abilityList

def dmgCalculator(inMove,pokemon):
		ability = getMove(Move)

'''
while True:
	for i in searchByName(input("Enter to search: ")):
		print(getByID(i))
'''

row = 0
col = 0
typeChart =  [
[1.0,1.0,1.0,1.0,1.0,0.5,1.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
[2.0,1.0,0.5,0.5,1.0,2.0,0.5,0.0,2.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,2.0,0.5],
[1.0,2.0,1.0,1.0,1.0,0.5,2.0,1.0,0.5,1.0,1.0,2.0,0.5,1.0,1.0,1.0,1.0,1.0],
[1.0,1.0,1.0,0.5,0.5,0.5,1.0,0.5,0.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0],
[1.0,1.0,0.0,2.0,1.0,2.0,0.5,1.0,2.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,1.0],
[1.0,0.5,2.0,1.0,0.5,1.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0],
[1.0,0.5,0.5,0.5,1.0,1.0,1.0,0.5,0.5,0.5,1.0,2.0,1.0,2.0,1.0,1.0,2.0,0.5],
[0.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,1.0],
[1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,0.5,0.5,1.0,0.5,1.0,2.0,1.0,1.0,2.0],
[1.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,2.0,0.5,0.5,2.0,1.0,1.0,2.0,0.5,1.0,1.0],
[1.0,1.0,1.0,1.0,2.0,2.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,1.0,0.5,1.0,1.0],
[1.0,1.0,0.5,0.5,2.0,2.0,0.5,1.0,0.5,0.5,2.0,0.5,1.0,1.0,1.0,0.5,1.0,1.0],
[1.0,1.0,2.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,0.5,1.0,1.0],
[1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0,0.5,1.0,1.0,0.0,1.0],
[1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,0.5,0.5,0.5,2.0,1.0,1.0,0.5,2.0,1.0,1.0],
[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,0.0],
[1.0,0.5,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,0.5],
[1.0,2.0,1.0,0.5,1.0,1.0,1.0,1.0,0.5,0.5,1.0,1.0,1.0,1.0,1.0,2.0,2.0,1.0]
]

while row < 18:
	col = 0
	while col < 18:	
		print(f'[{typeList[row]}][{typeList[col]}]: {typeChart[row][col]}')
		col = col + 1
	row = row + 1 

print(getPokeByID(10))
test = Pokemon(getPokeByID(10))


print(getAbility('Slash'))
