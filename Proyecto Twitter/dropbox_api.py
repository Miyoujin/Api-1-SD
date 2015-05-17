# Incluimos el SDK de Dropbox
import dropbox

# Funcion para escribir nuestros Tweets en un archivo en dropbox
def WriteDropbox(client, tweet):
    aux=client.search('/log/','logTwitter.txt')

    #Borramos el archivo local para que siempre este sincronizado con dropbox
    out = open('logTwitter.txt', "w")
    out.close()
    if len(aux) !=0:
        f, metadata = client.get_file_and_metadata('/log/logTwitter.txt')
        out.write(f.read())
        f.close()
    out.close()
    #Escribimos en el fichero
    tweet = tweet + '\n\n'
    tweet = tweet.encode('utf-8')
    f = open('logTwitter.txt', 'a')
    f.write(tweet)
    f.close()
    #Actualizamos el fichero que hay en dropbox, sino existe lo crea
    f = open('logTwitter.txt', 'rb')
    response = client.put_file('/log/logTwitter.txt', f,True)

# Funcion para escribir las busquedas realizadas en Twitter
def WriteDropboxSearch(client, Alltweet, nameFile):

  #Borramos el archivo local para que siempre este sincronizado con dropbox
  out = open(nameFile, "w")
  out.close()
  #Escribimos en el fichero
  Alltweet = Alltweet.encode('utf-8')
  f = open(nameFile, 'a')
  f.write(Alltweet)
  f.close()
  #Actualizamos el fichero que hay en dropbox, sino existe lo crea
  f = open(nameFile, 'rb')
  response = client.put_file('/log/'+nameFile, f,True)
