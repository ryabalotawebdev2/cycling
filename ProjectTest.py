from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class PageTest(unittest.TestCase):
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 self.assertIn("Owner's Registration",self.browser.title)

	def check_for_rows_in_listtable(self,row_text):
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_elements_by_tag_name('tr')
	 self.assertIn(row_text, [row.text for row in rows])



	def test_start_list_and_retrieve_it(self):
	 self.browser.get('http://localhost:8000/')
	 self.assertIn("Owner's Registration",self.browser.title)

	 headerText = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn("Owner's Registration", headerText)
	 inputbox = self.browser.find_element_by_id('pet')
	 self.assertEqual(inputbox.get_attribute('placeholder'), "Enter your pet name")
	 

	


	 name = self.browser.find_element_by_id('owner')
	 name.click()
	 time.sleep(1)
	 name.send_keys('Leonalyn Maglines')
	 time.sleep(1)
	 Address = self.browser.find_element_by_id('address')
	 Address.click()
	 time.sleep(1)
	 Address.send_keys('Blk 13 lot 10 brgy Dimawari')
	 time.sleep(1)
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('Shana')
	 time.sleep(1)
	 Breed = self.browser.find_element_by_id('breed')
	 Breed.click()
	 time.sleep(1)
	 Breed.send_keys('Puspin')
	 time.sleep(1)
	 Day = self.browser.find_element_by_id('birthday')
	 Day.click()
	 time.sleep(1)
	 Day.send_keys('08/22/2013')
	 time.sleep(1)
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
		#this page should update and show two types of id on the list
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('kuma')
	 time.sleep(1)
	 Breed = self.browser.find_element_by_id('breed')
	 Breed.click()
	 time.sleep(1)
	 Breed.send_keys('Pomeranian')
	 time.sleep(1)
	 Day = self.browser.find_element_by_id('birthday')
	 Day.click()
	 time.sleep(1)
	 Day.send_keys('05/25/2012')
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 self.check_for_rows_in_listtable('1: Shana Puspin born on 08/22/2013')
	 self.check_for_rows_in_listtable("1: kuma Pomeranian born on 05/25/2012")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')


	
if __name__=='__main__':
	 	unittest.main()


