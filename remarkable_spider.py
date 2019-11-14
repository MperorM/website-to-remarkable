# turn webpage into pdf 
import scrapy
import subprocess
import json
import remarkable_functions as rf

class RemarkableSpider(scrapy.Spider):
    '''
    Spider that trawls selected websites, and fills up json with links and titles.
    '''

    name = 'Remarkable Spider'
    link_json = {}

    def start_requests(self):
        with open('configuration.json', 'r') as f:
            configuration = json.load(f)
            for website in configuration:
                yield scrapy.Request(url=configuration[website]['website_link'], callback=self.scrape_sites, cb_kwargs={'website': website})


    def scrape_sites(self, response, website):
        with open('configuration.json', 'r') as f:
            configuration = json.load(f)
            post_links = configuration[website]['post_links_xpath']
            post_links = response.xpath(post_links).extract()
            post_names = configuration[website]['post_names_xpath']
            post_names = response.xpath(post_names).extract()
            files_to_upload = configuration[website]['files_to_upload']
            self.link_json[website] = []
            for i in range(0, files_to_upload):
                if post_links[0][0] == '/':
                    self.link_json[website].append((configuration[website]['raw_link'] + post_links[i], rf.sanitize_file_name(post_names[i])))
                else:
                    self.link_json[website].append((post_links[i], rf.sanitize_file_name(post_names[i])))
        with open('.links.json', 'w') as f:
            json.dump(self.link_json, f)