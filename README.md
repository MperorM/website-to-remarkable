# website-to-remarkable
A program for your remarkable tablet, that scrapes selected websites for new articles and uploads them as pdf's to your remarkable tablet. The program runs on macos and linux, windows is not supported.

# Setup 
The program makes use of [rmapi](https://github.com/juruen/rmapi) and requires rmapi to be set up in the same directory as the clone of this github.

rmapi can be downloaded [here](https://github.com/juruen/rmapi/releases). Download the file and unzip it. run the command

```
./rmapi
```
and follow the instructions to get the program synced with your remarkable tablet.

Then run
```
pip install -r requirements.txt 
```
this installs the required python packages.

Last we must install wkhtmltopdf. This is system specific.

#### Macos
Run
```
brew cask install wkhtmltopdf
```
If you do not have brew installed, you must first run
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
#### Debian/ubuntu
run
```
sudo apt-get install wkhtmltopdf
```
#### Arch
```
sudo pacman -S wkhtmltopdf
```

You are now ready to go!

# Adding a single webpage
Run
```
python3 single_website.py <website link> <name of remarkable file>
```
example

```
python3 single_website.py https://github.com/MperorM/website-to-remarkable github_page.pdf
```

The link will now be converted to a pdf and uploaded to your remarkable!

# Adding multiple articles from selected webpages
Run
```
python3 main.py
```
While the program is running you can turn on your remarkable and see the articles being added live.

# How do I make it scrape other websites?

To change the websites from which articles are downloaded, you must change the [configuration.json](configuration.json) file to include the website you want added, along with the xpath's that capture article links and names.

If you are unsure how to do this, write an issue with a request to add support for some website, and I will write it for you!

# How can I set it up to run automatically each day?
I like reading my remarkable papers in the morning before I touch my computer, using a chronjob you can set it up to run at certain times of day of your liking.

To do so type in your terminal:

```
cronjob -e
```

in here add the following line:

```
<minute of day> <hour of day> * * * cd <location of github clone> && <absolute python path> main.py
```
For example:
```
15 06 * * * cd ~/username/Desktop/website-to-remarkable && /usr/local/bin/python3 main.py
```
This will cause the articles to be downloaded at 06:15 each morning.
