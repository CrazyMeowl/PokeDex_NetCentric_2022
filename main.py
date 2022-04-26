import json
gen = input('Enter something: ')
gen = 1
while gen <= 7:
	data = json.load(open('resource/gen-'+ str(gen) +'.json'))
	#print(data)
	#Pokemon, Number, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Sprite
	for i in data:
		print(i['Pokemon'])
	gen = gen + 1
