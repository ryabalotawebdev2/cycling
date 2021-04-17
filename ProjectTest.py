
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.maximize_window()


	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Registration Form', self.browser.title)


#H1
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Welcome to my WebPage', headerText)



		#input for firstname
		label2 = self.browser.find_element_by_id('qwer').text
		self.assertIn('First name:', label2)
		firstname = self.browser.find_element_by_name('fname').send_keys("leonalyn")
		time.sleep(2)
		#input for firstname
		label3 = self.browser.find_element_by_id('hhhh').text
		self.assertIn('Last name:', label3)
		lastname = self.browser.find_element_by_name('lname').send_keys("maglines")
		time.sleep(2)

		sub = self.browser.find_element_by_id('Female').click()
		time.sleep(2)
		
		submitbutton = self.browser.find_element_by_name('clk').click()
		time.sleep(2)

		#submitbutton = self.browser.find_element_by_name('clkk').click()
		#time.sleep(2)



if __name__=='__main__':
	unittest.main()

#if _name__=='__main_':
	#unittest.main()





'''from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''

	

