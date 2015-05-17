import twitter

def searchKey(s,keys,count,nameFile,twitter_api,dropbox_api):

  results = twitter_api.search.tweets(q = s, count = count)

  for users in results["statuses"]:
    for k in keys:
      if keys in results["text"]:
        strings = users["user"]["screen_name"] + '\t' + results["text"]
        WriteDropboxSearch(client, string, nameFile)


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
