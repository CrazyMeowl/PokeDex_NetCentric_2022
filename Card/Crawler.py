
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

import json


'''
card = Card.find('xy1-1')
print(card)

json_object = json.dumps(card,default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
'''

print("Starting...")
cards= Card.all()
print(cards)
daList = []
#for card in cards:
    
    #daList.append(json_object)


json_object = json.dumps(cards,default=lambda o: o.__dict__, indent=4)

with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.write(str(cards))

print("Done....")
