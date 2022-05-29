import json
import os
import random

from pokemon import *
from ability import *
from type import *
#User 
#playername ,pokemon1id,pokemon2id,pokemon3id
def clear():
	os.system('cls')

def appendWithoutDuplicate(inList,inItem):
	if inItem not in inList:
		inList.append(inItem)
		
def randomPokemon():
	pokemonIdList = []
	while len(pokemonIdList) != 3:
		appendWithoutDuplicate(pokemonIdList,random.randint(0, 807))
	return pokemonIdList
def intinput(msg):
	while True:
		try:
			return int(input(msg))
		except:
			print("Please enter number!!!")
#
class User():
	def __init__(self,inName,inData):
		self.state = None
		self.name =  inName
		self.pokemon1 = Pokemon.getPokeByID(inData[0])
		self.pokemon2 = Pokemon.getPokeByID(inData[1])
		self.pokemon3 = Pokemon.getPokeByID(inData[2])
		self.pokemonList = [self.pokemon1,self.pokemon2,self.pokemon3]
		self.activePokemon = None
	def listPokemon(self):
		print(f"{self.name}'s pokemon:")
		i = 0 + 1
		while i < len(self.pokemonList) + 1:
			print(f'{i}|{self.pokemonList[i-1]["Name"]}') 
			i = i + 1

	def selectPokemon(self):
		self.listPokemon()
		pokemonIndex = intinput("Enter a pokemon id to select: ") - 1
		#print(pokemonIndex)
		if(self.pokemonList[pokemonIndex]['HP'] > 0):
			self.activePokemon = self.pokemonList[pokemonIndex]
			print('')
			print(f"You have selected {self.activePokemon['Name']} as your active pokemon.")
			print('')
			

	def listMoves(self):
		if(self.activePokemon == None):
			print("Have to select a pokemon")
		else:
			tempmoveList = [self.activePokemon['Ability1'],self.activePokemon['Ability2'],self.activePokemon['Ability3']]
			self.moveList = []
			for i in tempmoveList:
				if(i != 'none'):
					self.moveList.append(i)
			print(f"{self.activePokemon['Name']}'s abilities: ")
			if(len(self.moveList) != 0): 
				i = 0 + 1
				while i < len(self.moveList) + 1:
					print(f'{i}|{self.moveList[i-1]}') 
					i = i + 1
			else:
				print("NONE")
	def check(self):
		if self.activePokemon['HP'] <= 0:
			self.pokemonList.pop(self.pokemonList.index(self.activePokemon))
			if len(self.pokemonList) > 0:
				print('')
				print('Your active pokemon is dead!')
				print('')
				self.selectPokemon()
				return 'alive'
			else:
				self.state = "LOST"
				return 'dead'
		return 'alive'
	def removePokemon(self,index):
		self.pokemonList.pop(index)

	def setEnemy(self,someOne):
		self.enemy = someOne

	def attack(self):
		try:
			self.listMoves()
			move = intinput('Select your ability: ')
			chosenAbility = self.moveList[move-1]
			abiType = Ability.getType(chosenAbility)

		except Exception as bug:
			print(bug)
			chosenAbility = 'Punch'
			abiType = 'NORMAL'
			#'NORMAL'
		#print(chosenAbility)
		#print(abiType)
		msg = f"{self.activePokemon['Name']} used {chosenAbility} "
		dmgMultiplier = compareType(self.activePokemon['Type1'],self.enemy.activePokemon['Type1'])
		if dmgMultiplier == 1.0:
			msg = msg + "and it is not very effective "
		elif dmgMultiplier == 0.0:
			msg = msg + "and it doesn't work at all "
		elif dmgMultiplier == 0.5:
			msg = msg + "and it is not effective "
		elif dmgMultiplier == 2.0:
			msg = msg + "and it is very effective "

		dmg = (2 + random.randint(10,15)*(self.activePokemon['Attack']/self.enemy.activePokemon['Defense']))*dmgMultiplier
		print(dmg)

		self.enemy.activePokemon['HP'] = self.enemy.activePokemon['HP'] - dmg
		if self.enemy.activePokemon['HP'] > 0:
			msg = msg + f'and caused {dmg} damage'
		else:
			msg = msg + f'and killed {self.enemy.activePokemon["Name"]}'
		print(msg)
def switch(playerList,activePlayer):
	if activePlayer == playerList[0]:
		activePlayer = playerList[1]
	else:
		activePlayer = playerList[0]
	return activePlayer
def doTurn(player):
	print('')
	print(f"{player.name}'s Turn")
	if player.check() == "alive":
		player.attack()

		return('Done Turn')
	else:
		return('Lose')


#begin the process of getting info
clear()
player1name = input("Player 1 Name : ")
while True:
	clear()
	player1 = User(player1name,randomPokemon())
	player1.listPokemon()
	confirm = input("Do you want to use these pokemon (Y/N): ")
	if confirm.lower() == 'y':
		break
clear()
player2name = input("Player 2 Name : ")
while True:
	clear()
	player2 = User(player2name,randomPokemon())
	player2.listPokemon()
	confirm = input("Do you want to use these pokemon (Y/N): ")
	if confirm.lower() == 'y':
		break
# print(player1.pokemon1['HP'])
# player1.deploy(0)
# player1.activePokemon['HP'] = player1.activePokemon['HP'] - 10
# player1.deploy(1)
# player1.activePokemon['HP'] = player1.activePokemon['HP'] - 20

# print(player1.pokemon1['HP'])
playerList = []
activePlayer = None
clear()
print("The pokemon battle will now start with")
player1.listPokemon()
player2.listPokemon()
input('Enter to start playing!!!')
player1.setEnemy(player2)
player2.setEnemy(player1)
clear()
#first pokemon pick
player1.selectPokemon()
player2.selectPokemon()


playerList = [player1,player2]

if player1.activePokemon['Speed'] > player2.activePokemon['Speed']:
	activePlayer = player1
else:
	activePlayer = player2

while True:
	if (doTurn(activePlayer) == "Lose"):
		break
	else:
		activePlayer = switch(playerList,activePlayer)

print(f'{activePlayer.name} lost.')