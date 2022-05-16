from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/testing')
def pokedex():
	data = json.load(open('resource/all-gen.json'))
	theContent = ''
	for i in data:
		theContent = theContent +  f'<img src="{i["Sprite"]}" width="384" height="384" style="image-rendering:pixelated;">'
		for a in i:
			theContent = theContent + f'<p>{a}:{i[a]}</p>'
	theContent = theContent + '<br>'
	#return render_template("pokedex.html",content = theContent)
	return render_template('testing.html',thedex = theContent)

@app.route('/blurTesting')
def pokedexTesting():
	data = json.load(open('resource/all-gen.json'))
	theContent = ''
	for i in data:
		theContent = theContent +  f'<img src="{i["Sprite"]}" width="384" height="384">'
		for a in i:
			theContent = theContent + f'<p>{a}:{i[a]}</p>'
	theContent = theContent + '<br>'
	#return render_template("pokedex.html",content = theContent)
	return render_template('testing.html',thedex = theContent)

@app.route('/pokedex')
def testing():
	data = json.load(open('resource/all-gen.json'))
	theContent = ''
	firstItem = '<div class="carousel-item active"><img class="d-block w-100" src="###SOURCE###" style="image-rendering:pixelated;" alt="###NAME###"><div class="carousel-caption d-none d-md-block"><h5>###NAME###</h5><p>###INFO###</p></div></div>'
	otherItem = '<div class="carousel-item"><img class="d-block w-100" src="###SOURCE###" style="image-rendering:pixelated;" alt="###NAME###"><div class="carousel-caption d-none d-md-block"><h5>###NAME###</h5><p>###INFO###</p></div></div>'
	for i in data:
		pokeInfo = ''
		pokeInfo = pokeInfo + f'ID : {i["ID"]} '
		if data.index(i) == 0:
			theContent = theContent + firstItem.replace('###SOURCE###',i["Sprite"]).replace('###NAME###',i["Name"]).replace("###INFO###",pokeInfo)

		else:
			theContent = theContent + otherItem.replace('###SOURCE###',i["Sprite"]).replace('###NAME###',i["Name"]).replace("###INFO###",pokeInfo)

	return render_template('pokedex.html',thedex = theContent)


if __name__ == "__main__":
	app.run(debug=True)