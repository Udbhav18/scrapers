from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class insta_img:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome('chromedriver')

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/accounts/login')
        time.sleep(2)
        username_elem = self.driver.find_element(By.NAME, "username")
        username_elem.send_keys(username)
        password_elem = self.driver.find_element(By.NAME, "password")
        password_elem.send_keys(password)
        password_elem.submit()
        time.sleep(4)

    def get_img(self):
        self.driver.get(link)
        time.sleep(5)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        img = soup.find('img', class_='FFVAD')
        img_url = img['src']
        r = requests.get(img_url)
        with open("instagram"+str(time.time())+".png",'wb') as f: 
            f.write(r.content)
        self.driver.close()
        print('success')


if __name__ == '__main__':
    link = input("Enter Instagram Post URL: ")
    obj = insta_img(link)
    if input("Does the post belongs to a private account? (Y/N) : ") == 'Y' or 'y':
        username = input("Enter the username of your account to login: ")
        password = input("Enter the password of your account to login: ")
        obj.login(username, password)
    obj.get_img()