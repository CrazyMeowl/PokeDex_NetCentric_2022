import json
import os

#for i in pokemonData:
#	print(i['Pokemon'])
# Return a list of pokemon that match the search string

	
class Ability():
	#load ability data from json file
	data = json.load(open('resource/abilities.json'))
	#Move attribute: Name, Type, Category, Power, Accuracy, PowerPoint, Effect, Chance
	def __init__(self,inData):
		self.Name = inData['Name']
		self.Type = inData['Type']
		self.Category = inData['Category']
		self.Power = inData['Power']
		self.Accuracy = inData['Accuracy']
		self.PowerPoint = inData['PowerPoint']
		self.Effect = inData['Effect']
		self.Chance = inData['Chance']

	def getAll():
		return Ability.data
			
	def get(inString):
		for ability in Ability.data:
			if inString.lower() == ability['Name'].lower():
				return ability
				
	def searchByName(inString):
		abilityList = []
		for i in Ability.data:
			if inString.lower() in i['Name'].lower():
				abilityList.append(i['Name'])
		return abilityList


	def getType(inString):
		for ability in Ability.data:
			if inString.lower() == ability['Name'].lower():
				return ability['Type']
		print("Cant find that ability in database!!")
		return 'NORMAL'


