import tweepy, json, operator, time, dropbox, random, string, re
from GrabzIt import GrabzItClient
from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItPDFOptions

try:
    with open("keys.txt") as f:
        keys = f.read().splitlines() #read keys from the keys.txt file
except:
    print("Keys file not found")

pdf_path="actualOutput.pdf"
img_path="actualOutput.jpg"
random_file_name_length=10
access_token = keys[0]
access_token_secret = keys[1]
consumer_key = keys[2]
consumer_secret = keys[3]
pdfcrowd_api_key = keys[4]
grabzIt_key1 = keys[5]
grabzIt_key2 = keys[6]
dropbox_authkey = keys[7]

def dropbox_upload():
    dropbox_client = dropbox.Dropbox(dropbox_authkey)
    random_file_name = ''.join((random.choice(string.ascii_lowercase) for x in range(random_file_name_length)))
    dropbox_file_path = "/"+random_file_name+".pdf"
    f = open(pdf_path, 'rb')
    dropbox_client.files_upload(f.read(), dropbox_file_path)
    link=dropbox_client.sharing_create_shared_link(dropbox_file_path)
    url=link.url
    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
    return dl_url


def main():
    try:
        
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        grabzIt = GrabzItClient.GrabzItClient(grabzIt_key1, grabzIt_key2) #Using Grabzit API to convert tweet to image
        api=tweepy.API(auth,wait_on_rate_limit=True)
        latest_id=0
        while(True):
            tweets=api.mentions_timeline(max_count=3,include_rts=False,include_entries=False, since_ids=latest_id) #Search for bot mentions in timeline
            for i in range(len(tweets)):
                if(tweets[i].in_reply_to_status_id!=None and tweets[i].id>latest_id): #Checking if the tweet in which the bot is tagged is a reply to another tweet or not AND checking if the tag request is duplicate or not
                    if(tweets[i].id>latest_id):
                        latest_id = tweets[i].id
                    parent_tweet=api.get_status(tweets[i].in_reply_to_status_id) #Get parent tweet
                    print("USER "+tweets[i].user.screen_name+" SENT A REQUEST")
                    print(parent_tweet.user.screen_name+": "+parent_tweet.text)
                    str="https://twitter.com/twitter/statuses/"+parent_tweet.id_str #Get tweet embed code
                    html_code = (api.get_oembed(str)['html']) #Get the html code for the parent tweet
                    options = GrabzItImageOptions.GrabzItImageOptions() #Options for Image
                    options.browserWidth = 650 #Setting image width
                    grabzIt.HTMLToImage(html_code,options) #Convert html to image
                    grabzIt.SaveTo(img_path) #Save the generated image to file
                    grabzIt.HTMLToPDF(html_code) #Convert HTML to PDF
                    grabzIt.SaveTo(pdf_path) #Save generated PDF
                    dropbox_output_link=dropbox_upload() #Function to upload PDF to  Dropbox and generate the link
                    media = api.media_upload(filename=img_path) #create media object using jpg file
                    direct_message = api.send_direct_message(tweets[i].user.id, attachment_type='media', attachment_media_id=media.media_id,text="Here is the tweet that you requested! Tweet link: "+str)
                    direct_message = api.send_direct_message(tweets[i].user.id, text="And here is a download link to a pdf copy of the tweeet! "+dropbox_output_link)
                    str=""
            time.sleep(15)
    except Exception as e:
        print("ERROR OCCURED ")
        print(e)
        main()
main()