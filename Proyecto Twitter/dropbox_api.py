# Incluimos el SDK de Dropbox
import dropbox

def LoginInDropbox():
    # Claves de desarrollador de Dropbox
    app_key = 'lqmdjmalh5icz20'
    app_secret = 'xe4ssh1q9wr9vf9'

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()

    # Esto fallara si el usuario mete un codigo de autorizacion incorrecto
    access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient(access_token)

    return client

def WriteDropbox(client, tweet):
    aux=client.search('/log/','logTwitter.txt')

    #Borramos el archivo local para que siempre este sincronizado con dropbox
    out = open('logTwitter.txt', "w")
    #f.close()
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


def WriteDropboxSearch(client, nameTweet, nameFile)

  #Borramos el archivo local para que siempre este sincronizado con dropbox
  out = open(nameFile, "w")
  #f.close()
  #Escribimos en el fichero
  nametweet = nametweet + '\n\n'
  tweet = tweet.encode('utf-8')
  f = open(nameFile, 'a')
  f.write(tweet)
  f.close()
  #Actualizamos el fichero que hay en dropbox, sino existe lo crea
  f = open(nameFile, 'rb')
  response = client.put_file('/log/'+nameFile, f,True)
