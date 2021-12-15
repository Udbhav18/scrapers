from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

username = input('Enter your Username ')
password = input('Enter your Password ')
url = 'https://instagram.com/' + input('Enter username of user whome you want to send message')

def path():
	global chrome
	chrome = webdriver.Chrome('chromedriver')

def url_name(url):
    chrome.get(url)
    time.sleep(2)

def login(username, your_password):
	log_but = chrome.find_element_by_class_name("L3NKy")
	time.sleep(3)
	log_but.click()
	time.sleep(4)
	
	usern = chrome.find_element_by_name("username")
	usern.send_keys(username)

	passw = chrome.find_element_by_name("password")
	passw.send_keys(your_password)

	passw.send_keys(Keys.RETURN)
	time.sleep(5.5)
	
	notk = chrome.find_element_by_class_name("yWX7d")
	notk.click()
	time.sleep(3)

def send_message():
	message = chrome.find_element_by_class_name('_8A5w5 ')
	message.click()
	time.sleep(3)
	chrome.find_element_by_class_name('HoLwm ').click()
	time.sleep(3)
	l = ['Hello', 'Hi', 'This is a spam', 'This is cool lol']
	for x in range(30):
		mbox = chrome.find_element_by_tag_name('textarea')
		mbox.send_keys(random.choice(l))
		mbox.send_keys(Keys.RETURN)
		time.sleep(1.2)


path()
time.sleep(1)
url_name(url)
login(username, password)
send_message()
chrome.close()