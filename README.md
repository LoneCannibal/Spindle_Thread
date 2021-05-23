![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Spindle Thread Bot
A project we are working on to save Twitter threads when a Twitter user tags the bot in a thread they like. This bot will save tagged twitter threads in image format and PDF format. The image will be sent to the Twitter user requesting the thread via Twitter direct message. A dowload link to the PDF containing said Twitter thread will also be included.
## Team members
Aakash S D https://github.com/LoneCannibal/ <br/>
Ryan Hubert https://github.com/Zeno-san <br/>
Sanjay Satheesh https://github.com/Sanjay-Satheesh <br/>

To use this bot, follow the given instructions:

1. Just go to Twitter https://twitter.com and follow the bot @Spindle_Thread https://twitter.com/Spindle_Thread.
2. Now, go to the Twitter tweet that you want to save.
3. Tag the bot in the replies to the tweet, ie, reply to the tweet with the tag @Spindle_Thread.
4. In a few seconds, you will get an image of the tweet sent to your direct message (check your inbox). It will also contain a link to the thread. A download link will be provided if you wish to download a PDF of the tweet.

This bot uses the Tweepy API to function https://www.tweepy.org/.
It also uses the GrabzIt client https://pypi.org/project/GrabzIt/ to get an image of the tweet.
It also uses the DropBox API https://www.dropbox.com/developers/documentation/python to generate the download link for the PDF.

Having problems with the bot?

1. Yeah, I checked my direct message and didn't get any messages from the bot.

    Make sure you follow the bot. The bot can't send you messages unless you follow it or if you message it first. Go to https://twitter.com/Spindle_Thread and press the follow      button. Then follow step 3 in the instructions. Wait for 10-20 seconds to get the message.

2. The image I recieved isn't fully rendered. Where's the rest of my tweet?

    This is caused by problems in the GrabzIt API. Occassionally, the Javascript doesn't render completely. Not to worry, just request the tweet again and it'll be fixed.

3. The pdf I downloaded isn't fully rendered. There's only text here, where's my actual tweet??

    This is also caused by the same problem in the GrabzIt API. Occassionally, the Javascript doesn't render completely. Not to worry, just request the tweet again and it'll be fixed.

4. I have some other problem with the bot that isn't listed here!!! OR I tried everything, but it still doesn't seem to work

    Raise an issue here on Github and we'll get back to you in a few days(hopefully).
    
Other questions:

What's with the HTML page in the code?

We were originally working on a login page and website to work with this bot, but in the end we decided not to do it. We were just testing out the website. It's just a dummy webpage for now.
