from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/pokedex')
def pokedex():
	data = json.load(open('resource/all-gen.json'))
	finalHTML = ''
	for i in data:
		finalHTML = finalHTML +  f'<img src="{i["Sprite"]}" width="384" height="384" style="image-rendering:pixelated;">'
		for a in i:
			finalHTML = finalHTML + f'<p>{a}:{i[a]}</p>'
	finalHTML = finalHTML + '<br>'
	#return render_template("pokedex.html",content = finalHTML)
	return render_template('pokedex.html',thedex = finalHTML)

@app.route('/blurpokedex')
def pokedexTesting():
	data = json.load(open('resource/all-gen.json'))
	finalHTML = ''
	for i in data:
		finalHTML = finalHTML +  f'<img src="{i["Sprite"]}" width="384" height="384">'
		for a in i:
			finalHTML = finalHTML + f'<p>{a}:{i[a]}</p>'
	finalHTML = finalHTML + '<br>'
	#return render_template("pokedex.html",content = finalHTML)
	return render_template('pokedex.html',thedex = finalHTML)


if __name__ == "__main__":
	app.run(debug=True)