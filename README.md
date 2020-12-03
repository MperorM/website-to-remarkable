# website-to-remarkable

[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)][makeAPullRequest]
[![GitHub issues](https://img.shields.io/github/issues/MperorM/website-to-remarkable?style=flat-square)][issues]
![oses supported](https://img.shields.io/badge/platform-macos%20%7C%20linux-lightgray?style=flat-square)
![Languages supported](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue?style=flat-square)
[![GitHub license](https://img.shields.io/github/license/MperorM/website-to-remarkable?style=flat-square)][license]

A program for your reMarkable tablet, that scrapes selected websites for new articles and uploads them as PDFs to your reMarkable tablet. The program runs on macOS and Linux. Windows is not supported.


## Setup 
The program makes use of [`rmapi`][rmapi] and requires `rmapi` to be set up in the same directory as the clone of this GitHub repo.

`rmapi` can be downloaded [here][rmapi]. Download the file, unzip it and then run the command

```
$ ./rmapi
```

and follow the instructions to get the program synced with your reMarkable tablet.

Then run

```
$ pip install -r requirements.txt 
```

this installs the required Python packages.

Last, we must install [`wkhtmltopdf`][wkhtmltopdf]. This is system specific. Follow the instructions for your operating system.


<details>
<summary><b>macOS</b></summary>

Run

```bash
$ brew cask install wkhtmltopdf
```

If you do not have [`brew`][brew] installed, you must first run

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
</details>


<details>
<summary><b>Debian/Ubuntu</b></summary>

Run

```bash
$ sudo apt-get install wkhtmltopdf
```
</details>


<details>
<summary><b>Arch</b></summary>

Run

```bash
$ sudo pacman -S wkhtmltopdf
```
</details>


You are now ready to go!

## Adding a single webpage
Run

```bash
$ python3 single_website.py <website link> <name of remarkable file>
```

As an example, you could run

```bash
$ python3 single_website.py https://github.com/MperorM/website-to-remarkable github_page.pdf
```

The link will now be converted to a PDF and uploaded to your reMarkable!

## Adding multiple articles from selected webpages
Run

```bash
$ python3 main.py
```

While the program is running you can turn on your reMarkable and see the articles being added live.

## How do I make it scrape other websites?

To change the websites from which articles are downloaded, you must change the [configuration.json](configuration.json) file to include the website you want added, along with the XPaths that capture article links and names.

If you are unsure how to do this, write an issue with a request to add support for some website, and I will write it for you!

[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/MperorM/website-to-remarkable?style=social)][issuesCloded]



## How can I set it up to run automatically each day?
I like reading my reMarkable papers in the morning before I touch my computer. Using a cronjob you can set it up to run at certain times of day of your liking.

To do so type in your terminal:

```
$ cronjob -e
```

In here, add the following line:

```
<minute of day> <hour of day> * * * cd <location of cloned github repo> && <absolute python path> main.py
```

For example, you might run:

```
15 06 * * * cd ~/username/Desktop/website-to-remarkable && /usr/local/bin/python3 main.py
```

This will cause the articles to be downloaded at 06:15 each morning.


[license]: https://github.com/MperorM/website-to-remarkable/blob/master/LICENSE
[issues]: https://github.com/MperorM/website-to-remarkable/issues
[issuesCloded]: https://github.com/MperorM/website-to-remarkable/issues?q=is%3Aissue+is%3Aclosed
[wkhtmltopdf]: https://wkhtmltopdf.org
[rmapi]: https://github.com/juruen/rmapi/releases
[makeAPullRequest]: https://makeapullrequest.com
[brew]: https://brew.sh
