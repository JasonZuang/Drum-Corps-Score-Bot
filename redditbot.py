#! usr/bin/python
import praw

class RedditBot():
	
	def __init__(self,subreddit = ''):
		self.__conn__= praw.Reddit('test')
		self.__conn__.login('oldnewchefman','123456',disable_warning = True)
		print('login')
		self.subreddit = subreddit

	def post_thread(self):
		file = open('ready.txt','r')
		post = file.read()
		self.__conn__.submit(self.subreddit,'DCI Scores and Ranks',post)
		print(post)	

if __name__ =="__main__":
	bot = RedditBot('test')
	bot.post_thread()
