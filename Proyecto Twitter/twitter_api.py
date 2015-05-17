import tweepy
import dropbox_api


def searchKey(s,keys,count,nameFile,auth,client):

    api = tweepy.API(auth)
    results = api.search(q = s, rpp = count, show_user = True)

    out = open(nameFile, "w")
    out.close()
    Alltweet = ''
    for tweet in results:
        for k in keys:
            if k in tweet.text:
                tmp = '@'+tweet.user.screen_name + '\t' + tweet.text + '\n\n'
                Alltweet =  Alltweet + tmp
    dropbox_api.WriteDropboxSearch(client,Alltweet, nameFile)
