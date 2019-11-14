from scrapy.crawler import CrawlerProcess
import remarkable_spider as rs
import remarkable_functions as rf
import pdfkit
import os
import json
import subprocess

# remove files last loaded TODO: remove only old posts
try:
    with open('.links.json') as f:
        posts = json.load(f)
        for topic in posts:
            for post in posts[topic]:
                rf.remove_article(topic, post[1])
except:
    pass

# run webcrawler
process = CrawlerProcess({
    'LOG_LEVEL': 'CRITICAL' # change to INFO to debug spider
})
process.settings
process.crawl(rs.RemarkableSpider)
process.start()

# create remarkable folders and populate with articles
with open('.links.json') as f:
    posts = json.load(f)
    for topic in posts:
        proc = subprocess.Popen([f'./rmapi mkdir {topic}'], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        for post in posts[topic]:
            rf.create_and_upload_article(post[0], post[1], topic)