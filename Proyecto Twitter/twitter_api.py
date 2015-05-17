import tweepy
import dropbox_api


def searchKey(s,keys,count,nameFile,auth,client):

    api = tweepy.API(auth)
    public_tweets = api.home_timeline()

    out = open(nameFile, "w")
    out.close()

    for tweet in public_tweets:
         dropbox_api.WriteDropboxSearch(client, tweet.text, nameFile)



  #results = auth.search.tweets(q = s, count = count)

  #for users in results["statuses"]:
   # for k in keys:
    #  if keys in results["text"]:
     #   strings = users["user"]["screen_name"] + '\t' + results["text"]
      #  WriteDropboxSearch(client, string, nameFile)
