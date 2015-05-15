from flask import Flask, render_template
from flask import Flask, request

import webbrowser
import tweepy

consumer_key = 'dGuswhwb8LVKeVUcnDT3d8F3m'
consumer_secret = 'Jm78eJ1pVaM0pJXXr7MAMMQJNU1osGFSh4ONwZGYEfWc8Fo6Ww'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

app = Flask(__name__)

#Funcion que twittea introduciendo el pin y el tweet a poner
@app.route("/twitter", methods =['POST'])
def twitter():
    #Formularios del template
    pin = request.form['pin']


    token = auth.get_access_token(verifier=pin)
    auth.set_access_token(token[0], token[1])
    return render_template('tweetea.html')
@app.route("/twittear", methods = ['get'])
def twittear():
    #Escribimos tweet
    tweet = request.form['text']
    api = tweepy.API(auth)
    api.update_status(status=tweet)
    return render_template('exito.html')

#Obten aqui tu pin
@app.route("/loginTwitter")
def loginTwitter():
    webbrowser.open(auth.get_authorization_url())
    return index()

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
