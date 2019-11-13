# turn webpage into pdf 
import scrapy
import subprocess
import json
import remarkable_functions as rf

#TODO: eliminate boilerplate, make function that parses everything from a configuration.json
class RemarkableSpider(scrapy.Spider):
    '''
    Spider that trawls selected websites, and fills up json with links and titles.
    '''

    name = 'Remarkable Spider'
    link_json = {
        'ssc':        {'new': [], 'old': []},
        'hackernews': {'new': [], 'old': []},
        'eaforum':    {'new': [], 'old': []},
        'euobserver': {'new': [], 'old': []}
        }
    # get the links of last posts on slate star codex
    ssc = 'https://slatestarcodex.com/archives/'
    eaforum = 'https://forum.effectivealtruism.org/allPosts?sortedBy=new'
    hackernews = 'https://news.ycombinator.com'
    euobserver = 'https://euobserver.com/'

    def start_requests(self):
        yield scrapy.Request(url=self.ssc, callback=self.parse_ssc)
        yield scrapy.Request(url=self.eaforum, callback=self.parse_eaforum)
        yield scrapy.Request(url=self.hackernews, callback=self.parse_hackernews)
        yield scrapy.Request(url=self.euobserver, callback=self.parse_euobserver)


    def parse_ssc(self, response):
        post_links = response.xpath('//div[@class = "sya_postcontent"]/a/@href').extract()
        post_names = response.xpath('//div[@class = "sya_postcontent"]/a/text()').extract()
        posts_to_check = 3
        for i in range(0, posts_to_check):
            self.link_json['ssc']['new'].append((post_links[i], rf.sanitize_file_name(post_names[i])))
        with open('.links.json', 'w') as f:
            json.dump(self.link_json, f)
        

    def parse_eaforum(self, response):
        post_links = response.xpath('//span[@class = "PostsItem2-title"]/a/@href').extract()
        post_names = response.xpath('//span[@class = "PostsItem2-title"]/a/span[1]/text()').extract()
        posts_to_check = 3
        for i in range(0, posts_to_check):
            self.link_json['eaforum']['new'].append(('https://forum.effectivealtruism.org' + post_links[i], rf.sanitize_file_name(post_names[i])))
        with open('.links.json', 'w') as f:
            json.dump(self.link_json, f)

            
    def parse_hackernews(self, response):
        post_links = response.xpath('//a[@class = "storylink"]/@href').extract()
        post_names = response.xpath('//a[@class = "storylink"]/text()').extract()
        posts_to_check = 3
        for i in range(0, posts_to_check):
            self.link_json['hackernews']['new'].append((post_links[i], rf.sanitize_file_name(post_names[i])))
        with open('.links.json', 'w') as f:
            json.dump(self.link_json, f)


    def parse_euobserver(self, response):
        post_links = response.xpath('//h4[text() = "Latest News"]/following::ol/li/a/@href').extract()
        post_names = response.xpath('//h4[text() = "Latest News"]/following::ol/li/a/text()').extract()
        posts_to_check = 5
        for i in range(0, posts_to_check):
            self.link_json['euobserver']['new'].append((self.euobserver[:-1] + post_links[i], rf.sanitize_file_name(post_names[i])))
        with open('.links.json', 'w') as f:
            json.dump(self.link_json, f)