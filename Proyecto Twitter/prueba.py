import LoginDropbox

client = LoginDropbox.LoginInDropbox()
print 'linked account: ', client.account_info()
