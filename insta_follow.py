from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/scratchedstories/followers/')
time.sleep(3)
username = browser.find_elements_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
username[0].send_keys('enter your email id or username here')#enter your email id or username here
password = browser.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
password.send_keys('Enter your password here')#Enter your password here
password.send_keys(Keys.ENTER)
time.sleep(7)
follower_link = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a')
follower_link.click()
time.sleep(3)
follow_links = browser.find_elements_by_tag_name('button')
number_of_follow = 10 # enter the number of people you want to follow
for i in range(4,4+number_of_follow):
   follow_links[i].click()
   time.sleep(round(random.uniform(5,8.99),2))

