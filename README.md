# Spindle Thread Bot
A project we are working on to save Twitter threads.
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
