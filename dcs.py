#! usr/bin/python
from crawler import crawler
from redditbot import RedditBot
from textbot import textbot


crawler = crawler()
crawler.download_html(crawler.get_show_list_url())
crawler.get_names()

bot = RedditBot('test')
bot.post_thread()

bot = textbot('ACea3dd6dd6390948521e1d97074c568bb','0c1a90ab34b4d1ea6b74d818f3c75e65'
,'4697349239','4698045152')
bot.sendMessage()
