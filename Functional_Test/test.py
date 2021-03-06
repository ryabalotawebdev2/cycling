from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

RayRay_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 #elf.browser.get('http://localhost:8000/')
	 self.browser.get(self.live_server_url)
	 self.assertIn('SYSTEM',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn('Event Registration', header_text)
	 
	 
	 
	
	 inputemail = self.browser.find_element_by_id('email')
	 self.assertEqual(inputemail.get_attribute('placeholder'),'Enter your email')
	 inputemail.click()
	 time.sleep(1)
	 inputemail.send_keys('Ryanbalota@gmail.com')
	 
	 time.sleep(1)
	 
	 
	 inputfull = self.browser.find_element_by_id('fullname')
	 self.assertEqual(inputfull.get_attribute('placeholder'),'Enter your fullname')
	 inputfull.click()
	 time.sleep(1)
	 inputfull.send_keys('Ryanbalota')
	 time.sleep(1)
	 
	 
	 btnConfirm = self.browser.find_element_by_id('btnConfirm')
	 btnConfirm.click()
	 time.sleep(2)
	 


	


'''	

if __name__=='__main__':
	 	unittest.main()
#this page should update and show two types of id on the list
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('Kuma')
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
	 #self.assertIn('1: Shana Puspin born on 08/22/2013',[row.text for row in rows])
	 #self.assertIn('1: Kuma Pomeranian born on 05/25/2012',[row.text for row in rows])
	 self.check_for_rows_in_list_table('1: Shana Puspin born on 08/22/2013')
	 self.check_for_rows_in_list_table("1: Kuma Pomeranian born on 05/25/2012")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')
'''
