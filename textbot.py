#! usr/bin/python
from twilio.rest import TwilioRestClient

class textbot():
	
	def __init__(self,sid,token,number,tnumber):
		self.__SID__ = sid
		self.__token__= token
		self.__number__ = number
		self.__tnumber__ = tnumber
	
	def sendMessage(self):
		file = open('ready.txt','r')
		message = file.read()
		cli = TwilioRestClient(self.__SID__,self.__token__)
		cli.messages.create(body=message,from_=self.__tnumber__,to_=self.__number__)
		file = open('perc.txt','r')
		message = 'Percussion: '+file.read()
		cli.messages.create(body=message,from_=self.__tnumber__,to_=self.__number__)

if __name__ =="__main__":
	bot = textbot('ACea3dd6dd6390948521e1d97074c568bb','0c1a90ab34b4d1ea6b74d818f3c75e65'
,'4697349239','4698045152')
	bot.sendMessage()
