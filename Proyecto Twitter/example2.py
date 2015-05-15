# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'lqmdjmalh5icz20'
app_secret = 'xe4ssh1q9wr9vf9'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#Aqui comprobamos si el archivo existe en dropbox, sino existe lo creamos en local
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

f = open('magnum-opus.txt', 'a')
f.write(' ADRIAAAAAAN\n')
f.close()

#Actualizamos el fichero que hay en dropbox, sino existe lo crea
f = open('magnum-opus.txt', 'rb')

response = client.put_file('/log/magnum-opus.txt', f,True)
#print 'uploaded: ', response

folder_metadata = client.metadata('/')
#print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/log/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
#print metadata
