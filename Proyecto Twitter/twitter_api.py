import twitter


def searchKey(s,keys,count,nameFile,twitter_api,dropbox_api):

  results = twitter_api.search.tweets(q = s, count = count)

  for users in results["statuses"]:
    for k in keys:
      if keys in results["text"]:
        strings = users["user"]["screen_name"] + '\t' + results["text"]
        WriteDropboxSearch(client, string, nameFile)
