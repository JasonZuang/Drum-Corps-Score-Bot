#! /usr/bin/python

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class crawler:
	'''
	This crawler goes onto the dci website, searches for the scores and then downloads the recaps. 
	BeautifulSoup parses it and extracts the name of the corps and the scores
	'''
	def __init__(self):
		pass
	
	def get_show_list_url(self):
		driver = webdriver.Firefox()
		url = 'http://www.dci.org/ViewArticle.dbml?ATCLID=210133434'
		driver.get(url)
		venue = driver.find_element_by_class_name("event")
		venue.click()
		div = driver.find_element_by_class_name("roundName")
		return driver.find_element_by_link_text("View Recap").get_attribute("href")
	

	def download_html(self, url):
		res = requests.get(url)
		res.raise_for_status()
		file = open('scores.txt','wb')
		file.write('\n')
		file.write(res.text)
			
	def get_names(self):
		#do math for all scores
		file = open('scores.txt','r')
		soup = BeautifulSoup(file.read())
		corps = soup.findAll('td',{"class":"content topBorder rightBorderDouble"})
		score = soup.findAll('td',{"class":"content score"})
		rank = soup.findAll('td',{"class":"content rank"})
		file = open('ready.txt','wb')
		file2 = open('perc.txt','wb')
		for x in range (len(corps)):
			a = (-1 + ((x+1)*(len(score)/len(corps))))
			string = (corps[x].getText()+' '+score[a].getText()+' '+rank[a].getText()+'\n')
			file.write(string)
			print(string)
			string = (corps[x].getText()+' '+score[a-5].getText()+' '+rank[a-5].getText()+'\n')
			file2.write(string)
			print(string)
	
	
if __name__ =="__main__":
	wcrawler = crawler()
	wcrawler.download_html(crawler.get_show_list_url())
	wcrawler.get_names()
	
