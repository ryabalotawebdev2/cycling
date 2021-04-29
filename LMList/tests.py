from django.test import TestCase
#from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import HttpRequest
#from django.urls import resolve


class HomePageTest(TestCase):

	#def test_root_url_resolve_to_homepage_view(self):
		#found = resolve('/')

	def test_homepage_returns_correct_views(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'owner': 'pet'})
		self.assertIn('pet', response.content.decode())
		self.assertTemplateUsed(response,'homepage.html')


	


	'''def test_homepage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')'''



	'''def test_homepage_returns_correct_view(self):
		request = HttpRequest()
		response = HomePageTests(request)
		#html = response.content.decode('utf8')
		string_html = render_to_string('homepage.html')
		self.assertEqual(html, string_html)'''

	#def test_homepage_returns_correct_view(self):
		#request = HttpRequest()
		#reponse = HomePage(request)
		#html = response.content.decode('utf8')
		#string_html = render_to_string('homepage.html')
		#self.assertEqual(html, string_html)


		

	'''def test_save_POST_request(self):
		reponse = self.client.post('/', data={'pet': 'New entry'})
		newItem = Item.objects.first()
		self.assertEqual(newItemtext, 'New entry')
		self.assertIn('New entry', reponse.content.decode())
		self.assertTemplateUsed(reponse, 'homepage.html')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_save_POST_request(self):
		reponse = self.client.post('/', data={'pet': 'leo'}) 
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'leo')

	def test_redirects_POST(self):
		reponse = self.client.post('/', data={'pet': 'leo'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_template_display_list(self):
		Item.objects.create(text='List item 1')
		Item.objects.create(text='List item 2')
		response = self.client.get('/')
		self.assertIn('List item 1', response.content.decode())
		self.assertIn('List item 2', response.content.decode())
	

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')'''