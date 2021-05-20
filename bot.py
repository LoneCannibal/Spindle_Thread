import tweepy, json, operator, time
from GrabzIt import GrabzItClient

def main():
    try:
        with open("keys.txt") as f:
            keys = f.read().splitlines() #read keys from the keys.txt file
        access_token=keys[0]
        access_token_secret=keys[1]
        consumer_key=keys[2]
        consumer_secret=keys[3]
        pdfcrowd_api_key=keys[4]
        auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        grabzIt = GrabzItClient.GrabzItClient(keys[5], keys[6]) #Using Grabzit API to convert tweet to image
        api=tweepy.API(auth,wait_on_rate_limit=True)
        latest_id=0
        while(True):
            tweets=api.mentions_timeline(max_count=3,include_rts=False,include_entries=False, since_ids=latest_id) #Search for bot mentions in timeline
            for i in range(len(tweets)):
                if(tweets[i].in_reply_to_status_id!=None and tweets[i].id>latest_id): #Checking if the tweet in which the bot is tagged is a reply to another tweet or not AND checking if the tag request is duplicate or not
                    if(tweets[i].id>latest_id):
                        latest_id=tweets[i].id
                        
                    parent_tweet=api.get_status(tweets[i].in_reply_to_status_id) #Get parent tweet
                    print("USER "+tweets[i].user.screen_name+" SENT A REQUEST")
                    print(parent_tweet.user.screen_name+": "+parent_tweet.text)
                    str="https://twitter.com/twitter/statuses/"+parent_tweet.id_str #Get tweet embed code
                    #client = pdfcrowd.HtmlToImageClient('lonecannibal', pdfcrowd_api_key)
                    #client.setOutputFormat('jpg')
                    #client.convertUrlToFile(str, 'actualOutput.jpg')
                    html_code=(api.get_oembed(str)['html']) #Get the html code for the parent tweet
                    grabzIt.HTMLToImage(html_code) #Convert html to image
                    grabzIt.SaveTo("actualOutput.jpg") #Save the generated image to file
                    #imgkit.from_url(str,'actualOutput.jpg',options={'javascript-delay':'4000', 'height':'600'}) #convert tweet to jpg
                    media = api.media_upload(filename='actualOutput.jpg') #create media object using jpg file
                    direct_message = api.send_direct_message(tweets[i].user.id, attachment_type='media', attachment_media_id=media.media_id,text="Here is the tweet that you requested! Tweet link: "+str)
                    str=""
            time.sleep(15)
    except Exception as e:
        print("ERROR OCCURED "+e)
        main()
main()