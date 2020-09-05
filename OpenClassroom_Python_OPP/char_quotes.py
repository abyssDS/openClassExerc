import json
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

EOF

def read_values_from_json(file, key):
	#Create a new empty list
	my_list=[]

	#open a json file with my objects
	with open("characters.json") as f:

		#load all the data contained in this file. data = entries
		data = json.load(f)

		#add each item in my list
		for entry in data:
			my_list.append(entry[key])

	#return my completed list
	return my_list
