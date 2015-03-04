import string
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
def parse_it_asap(song):
	string = str(song)
	parsed = ''
	for char in string:
		if char == ' ':
			char = '+'
		parsed = parsed + char

	url = 'http://www.google.com/search?q=' + 'site:azlyrics.com+' + parsed

	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	href_list = []
	i = 0
	for a in soup.find_all('a', href=True):
		href_list.append(a)
	blurURL = str(href_list[24])
	blurURL = blurURL[16:]
	sep = 'html'

	hello = blurURL.split(sep)[0]
	url = hello + 'html'

	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	divs = soup.find_all("div")
	div_list = []
	for div in divs:
	    div_list.append(div)
	lyrics = div_list[6]    

	text = str(lyrics)
	driver = webdriver.PhantomJS()
	driver.set_window_size(1280, 1024) # set browser size.
	driver.get('http://www.freesummarizer.com') # Load page
	summarize_box = driver.find_element_by_xpath('//*[@id="summarizebutton"]/i')
	# time.sleep(1)
	summarize_box.click()
	#driver.save_screenshot('github.png')

	text_box = driver.find_element_by_xpath('//*[@id="text"]')
	time.sleep(1)
	text_box.clear()
	text_box.send_keys(text)
	text_box.send_keys(Keys.ESCAPE)

	m_sentences = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/input[2]')
	# time.sleep(5)
	m_sentences.clear()
	# time.sleep(5)
	m_sentences.send_keys('1')

	email = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/input[3]')
	# time.sleep(5)
	email.send_keys('ulises.giacoman@gmail.com')

	submit = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/div/input')
	submit.click()

	summary2 = driver.find_element_by_class_name('summary2').text
	summary2 = str(summary2)
	summary2 = summary2[21:]
	summary2 = summary2.partition('Want')
	return str(summary2[0])

if __name__ == "__main__":
	print(parse_it_asap(song))

