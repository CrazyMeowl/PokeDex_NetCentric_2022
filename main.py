import json
import os
import random

from pokemon_file import *
from ability_file import *

#User 
class User():
	def __init__(self,inData):
		pass

#Type things here
typeList = ['NORMAL','FIGHTING','FLYING','POISON','GROUND','ROCK','BUG','GHOST','STEEL','FIRE','WATER','GRASS','ELECTRIC','PSYCHIC','ICE','DRAGON','DARK','FAIRY'] 
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
# inType1 == AttackType , inType2 == DefendType
def compareType(inType1,inType2):
	return typeChart[typeList.index(inType1)][typeList.index(inType2)]




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
		if inString.lower() == ability['Name'].lower():
			return ability
def searchAbilitiesByName(inString):
	abilityList = []
	for i in abilityData:
		if inString.lower() in i['Name'].lower():
			abilityList.append(i['Name'])
	return abilityList

def dmgCalculator(inMove,pokemon):
		ability = getMove(Move)

def appendWithoutDuplicate(inList,inItem):
	if inItem not in inList:
		inList.append(inItem)

'''
while True:
	for i in searchByName(input("Enter to search: ")):
		print(getByID(i))
'''


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

#print(getAbility('Sleep Powder'))
#print(compareType('NORMAL','STEEL'))
#Important stuff
# if random.randint(0,100) < 36:
#     do_stuff()
abiTypeList = []
for i in Ability.getAll():
	appendWithoutDuplicate(abiTypeList,i['Type'])
print(abiTypeList)
print(len(abiTypeList))