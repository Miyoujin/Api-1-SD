import dropbox


def WriteDropbox(client, tweet):
    aux=client.search('/log/','magnum-opus.txt')

    print "     Print aux         "
    print aux
    #Borramos el archivo local para que siempre este sincronizado con dropbox
    f = open('magnum-opus.txt', "w")
    f.close()
    if len(aux) !=0:
        f, metadata = client.get_file_and_metadata('/log/magnum-opus.txt')
        out = open('magnum-opus.txt', "w")
        out.write(f.read())
        out.close()
        f.close()
    #Escribimos en el fichero
    tweet = tweet + '\n\n'
    tweet = tweet.encode('utf-8')
    f = open('magnum-opus.txt', 'a')
    f.write(tweet)
    f.close()
    #Actualizamos el fichero que hay en dropbox, sino existe lo crea
    f = open('magnum-opus.txt', 'rb')
    response = client.put_file('/log/magnum-opus.txt', f,True)
