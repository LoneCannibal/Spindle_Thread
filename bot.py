import tweepy,json,operator, time

def main():
    with open("keys.txt") as f:
        keys = f.read().splitlines() 
    access_token=keys[0]
    access_token_secret=keys[1]
    consumer_key=keys[2]
    consumer_secret=keys[3]
    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    while(True):
        statuses=api.mentions_timeline(count=3,include_rts=False,include_entries=False)
        for i in range(len(statuses)):
            print(statuses[i].text)
            str="https://twitter.com/twitter/statuses/"+statuses[i].id_str
            print(api.get_oembed(str))
            str=""
        time.sleep(10)
main()