import re
import requests
import argparse

import jsonpickle
from bs4 import BeautifulSoup
from flask import Flask, request, Response, jsonify


app = Flask(__name__)



def preprocess(string):
	"""Return preprocessed string
		
		Args:
			string (str): messy/noisy string
			
		Returns:
			pp_string (str): clean string without unicode characters
	"""
	string = re.sub(r"\n", "", string)
	pp_string = string.strip()
	
	return pp_string

def make_url(author_name):
	"""Return reformatted url
		
		Args:
			author_name (str): name of the author
			
		Returns:
			url (str): reformatted url for a given author
	"""
	if len(author_name.split()) == 1:
		url = "https://www.thehindu.com/search/?q=a&order=DESC&sort=publishdate&au={}".format(author_name)
		
	else:
		author_name = "%20".join([i.capitalize() for i in author_name.split()])
		url = "https://www.thehindu.com/search/?q=a&order=DESC&sort=publishdate&au={}".format(author_name)
		
	return url
	
def get_articles(name):
	"""Return articles of author in descending order of date.
	
		Args:
			name (str): Name of the author
			
		Returns:
			author_articles (dict): contains metadata (name, date) along with links to the articles
	"""
	author_articles = {}
	author_articles['name'] = " ".join([i.capitalize() for i in name.split()])
	author_articles['articles'] = list()
	
	ht_url = make_url(name)
	url = requests.get(ht_url)
	
	if url.status_code == 200:

		ht_tags = BeautifulSoup(url.content, 'html.parser')
		articles = ht_tags.find_all("a", {"class": "story-card-img focuspoint"})
		dates = ht_tags.find_all("span", {"class": "dateline"})
		article_names = ht_tags.find_all("a", {"class":"story-card75x1-text"})
		article = dict()

		for idx, (date, links, title) in enumerate(zip(dates, articles, article_names)):

			new_article = {}

			new_article["date"] = date.text
			new_article["link"] = links['href']
			title = preprocess(title.text)
		
			article[title] = new_article

		author_articles['articles'] = [article]
		
		return author_articles
		
	return author_articles


@app.route('/', methods=['GET', 'POST'])
def articles():
	if request.method == 'GET':
		return 'OK'


	elif request.method == 'POST':
		name = request.form.get("author_name")
		response = get_articles(name)
		#return Response(response, status=200, mime_type='application/json')
		return jsonify(response)
	else:
		return Response(response=jsonpickle.encode({'date': None}), status=200, mimetype="application/json")	


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	
	
