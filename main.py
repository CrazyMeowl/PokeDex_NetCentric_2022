import json
import os
data = json.load(open('resource/all-gen.json'))

pokemonData = json.load(open('resource/all-gen.json'))
moveData = json.load(open('resource/moves.json'))
typeList = ['NORMAL','FIGHTING','FLYING','POISON','GROUND','ROCK','BUG','GHOST','STEEL','FIRE','WATER','GRASS','ELECTRIC','PSYCHIC','ICE','DRAGON','DARK','FAIRY'] 
#Name, ID, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Sprite
genIdList = [(1,151),(152,251),(252,386),(387,493),(494,649),(650,721),(722,807)]
#for i in pokemonData:
#	print(i['Pokemon'])
# Return a list of pokemon that match the search string


def searchPokeByName(inString):
	idList = []
	for i in pokemonData:
		if inString.lower() in i['pokemon'].lower():
			idList.append(i['ID'])
	return idList
#get pokemon name by id return info string
def getPokeByID(inId):
	chosenOne = pokemonData[inId-1]
	info = ""
	for i in chosenOne:
		info = info + "%10s :  %s  \n"%(i,str(chosenOne[i]))
	#print(info)
	return info

def getGen(gen):

	startId,endId = genIdList[gen-1]
	for i in range(startId,endId+1):
		print(getPokeByID(i))

def getMoves():
	for i in moveData:
		for a in i:
			print(a,":",i[a],end="|")
		print()
def getMove(moveName):
	for move in moveData:
		if inString.lower() in move['Name'].lower():
			return move
def getMoveByName(inString):
	moveList = []
	for i in moveData:
		if inString.lower() in i['Name'].lower():
			moveList.append(i['Name'])
	return moveList

def dmgCalculator(inMove,pokemon):
		move = getMove(Move)

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

