# website-to-remarkable
A program for your remarkable tablet, that crawls selected websites for new articles and uploads them as pdf's to your remarkable tablet. The program runs on macos and linux, windows is not supported.

# Setup 
The program makes use of [rmapi](https://github.com/juruen/rmapi) and requires rmapi to be set up in the same directory as the clone of this github.

rmapi can be downloaded [here](https://github.com/juruen/rmapi/releases). Download the file and unzip it. run the command

```
./rmapi
```
and follow the instructions to get the program synced with your remarkable tablet.

Once it is set up, all you need to do is run
```
python main.py
```

While the program is running you can turn on your remarkable and see the articles being added live.

# How can I change to other websites?

To change the websites from which articles are downloaded, you must rewrite the [remarkable_spider.py](remarkable_spider.py) to trawl different websites.

if you are unsure how to do this, write an issue with a request to add support for some website, and I will write it for you!

# How can I set it up to run automatically each day?
I like reading my remarkable papers in the morning before I touch my computer, using a chronjob you can set it up to run at certain times of day of your liking.

To do so type in your terminal:

```
cronjob -e
```

in here add the following line:

```
0 21 * * * cd <location of github clone> && /usr/local/bin/python3 main.py
```

This will cause the articles to be downloaded at 21:00 each night. To change it to some other time of your liking, replace the first zero with whichever minute of the day you want and the 21 with whichever hour.
