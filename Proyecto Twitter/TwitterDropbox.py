from flask import Flask, render_template
from flask import Flask, request

import datetime
import webbrowser
import tweepy
import dropbox
import dropbox_api
import twitter_api

logueado = False
tLog = datetime.datetime.now()


# Twitter
consumer_key = 'dGuswhwb8LVKeVUcnDT3d8F3m'
consumer_secret = 'Jm78eJ1pVaM0pJXXr7MAMMQJNU1osGFSh4ONwZGYEfWc8Fo6Ww'

# Dropbox
app_key = 'lqmdjmalh5icz20'
app_secret = 'xe4ssh1q9wr9vf9'

app = Flask(__name__)

# Al principio de cada funcion comprobamos
# siempre el tiempo por si expira el tiempo de la clave

@app.route("/twitter")
def menu():
    global logueado
    compruebaTiempo()
    if logueado == False:
        return index()
    else:
        return render_template('menu.html')

#Funcion para loguearnos en Twitter y en Dropbox
@app.route("/twitter", methods =['POST'])
def twitter():
    global client
    global logueado
    global auth
    global tLog

    #Formularios del template
    pint = request.form['pint']
    pind = request.form['pind']

    token = auth.get_access_token(verifier=pint)
    auth.set_access_token(token[0], token[1])

    access_token, user_id = flow.finish(pind)
    client = dropbox.client.DropboxClient(access_token)

    logueado = True
    tLog = datetime.datetime.now()

    return menu()

# Comprobamos que no ha expirado el tiempo de la clave
@app.route("/tweetea")
def tweetea():
    global logueado
    compruebaTiempo()
    if logueado == False:
        return index()
    else:
        return render_template('tweetea.html')

# Comprobamos que no ha expirado el tiempo de la clave
@app.route("/searchKey")
def sKey():
    global logueado
    compruebaTiempo()
    if logueado == False:
        return index()
    else:
        return render_template('searchKey.html')

# Codigo para buscar en Twitter
@app.route("/searchKey", methods =['POST'])
def buscaKey():
    global logueado
    global auth

    compruebaTiempo()
    if logueado == False:
        return index()
    else:
        # Parametros para buscar
        s = request.form['tema'];
        keys = request.form['pClave']
        keys = keys.split(',', len(keys))
        count = request.form['count']
        nameFile = request.form['nombre']
        # Llamamos a la funcion para buscar en Twitter
        twitter_api.searchKey(s,keys,count,nameFile,auth,client)

        return render_template('exitoDrop.html')

# Codigo para Twittear
@app.route("/twittear", methods = ['POST'])
def twittear():
    global logueado
    global auth

    #Escribimos tweet
    tweet = request.form['tweet']
    # Publicamos el Tweet
    api = tweepy.API(auth)
    api.update_status(status=tweet)
    # Escribimos en Dropbox el Tweet
    dropbox_api.WriteDropbox(client,tweet)

    compruebaTiempo()
    if logueado == False:
        return index()
    else:
        return render_template('exito.html')


# Codigo donde se piden los pin para loguearse en Twitter y Dropbox
@app.route("/")
def index():
    global logueado
    compruebaTiempo()
    if logueado == True:
        return menu()
    else:
        global auth
        global flow
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        urlTwitter = auth.get_authorization_url()
        urlDropbox = flow.start()
        return render_template('index.html', urlTwitter=urlTwitter, urlDropbox=urlDropbox)

# Funcion para comprobar el tiempo por si expira la clave
def compruebaTiempo():
    global tLog
    global logueado

    tNow = datetime.datetime.now()

    if (tNow - tLog).seconds > 299:
        logueado = False

if __name__ == "__main__":
    app.run(debug=True)
