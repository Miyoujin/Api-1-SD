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
