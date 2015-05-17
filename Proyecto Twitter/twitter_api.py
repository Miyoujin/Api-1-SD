import tweepy
import dropbox_api


# Funcion para buscar en Twitter segun un tema (s) y unas claves (keys)
def searchKey(s,keys,count,nameFile,auth,client):

    # Hacemos la busqueda
    api = tweepy.API(auth)
    results = api.search(q = s, rpp = count, show_user = True)

    # Vamos guardando en Alltweet todas las busquedas con el usuario responsable
    Alltweet = ''
    for tweet in results:
        for k in keys:
            if k in tweet.text:
                tmp = '@'+tweet.user.screen_name + '\t' + tweet.text + '\n\n'
                Alltweet =  Alltweet + tmp
    # Por ultimo escribimos todo lo recolectado en un archivo en Dropbox
    dropbox_api.WriteDropboxSearch(client,Alltweet, nameFile)
